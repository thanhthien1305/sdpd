import { describe, it, expect } from 'vitest';
import { computeNodes, computeEdges, sumMetrics } from './useChaosSimulator';
import type { ChaosFault, ChaosFix, ChaosMetrics } from '../types/chaos';
import type { DiagramEdge, DiagramNode } from '../types/case';

const dummyNode = (id: string): DiagramNode => ({
  id,
  type: 'server',
  label: id,
  status: 'healthy',
  position: { x: 0, y: 0 },
  inspectable: false,
});

const dummyEdge = (id: string, source = 'n1', target = 'n2'): DiagramEdge => ({
  id,
  source,
  target,
  style: 'normal',
  animated: false,
});

const nodeCrashFault: ChaosFault = {
  id: 'node-crash',
  nameKey: 'fault.nodeCrash',
  descriptionKey: '',
  severity: 'high',
  targets: { nodes: ['api'] },
  effects: { availability: -4 },
  logTemplates: [],
};

const cacheMissFault: ChaosFault = {
  id: 'cache-miss-storm',
  nameKey: 'fault.cacheMiss',
  descriptionKey: '',
  severity: 'medium',
  targets: { nodes: ['cache'] },
  effects: { latency: 160 },
  logTemplates: [],
};

const packetLossFault: ChaosFault = {
  id: 'packet-loss',
  nameKey: 'fault.packetLoss',
  descriptionKey: '',
  severity: 'high',
  targets: { edges: ['e1'] },
  effects: { errorRate: 2.5 },
  logTemplates: [],
};

const latencySpikeFault: ChaosFault = {
  id: 'latency-spike',
  nameKey: 'fault.latencySpike',
  descriptionKey: '',
  severity: 'medium',
  targets: { edges: ['e2'] },
  effects: { latency: 200 },
  logTemplates: [],
};

const circuitBreakerFix: ChaosFix = {
  id: 'enable-circuit-breaker',
  nameKey: 'fix.circuitBreaker',
  descriptionKey: '',
  counters: ['node-crash', 'db-primary-fail'],
  effects: { errorRate: -1.5 },
  logTemplates: [],
};

const cacheWarmupFix: ChaosFix = {
  id: 'cache-warmup',
  nameKey: 'fix.cacheWarmup',
  descriptionKey: '',
  counters: ['cache-miss-storm'],
  effects: { latency: -100 },
  logTemplates: [],
};

const retriesFix: ChaosFix = {
  id: 'add-retries',
  nameKey: 'fix.addRetries',
  descriptionKey: '',
  counters: ['packet-loss', 'latency-spike'],
  effects: { errorRate: -1 },
  logTemplates: [],
};

describe('computeNodes', () => {
  const baseNodes = [dummyNode('api'), dummyNode('cache'), dummyNode('db')];

  it('leaves nodes healthy when no faults are active', () => {
    const nodes = computeNodes(baseNodes, [], []);
    expect(nodes.every((n) => n.status === 'healthy')).toBe(true);
  });

  it('marks node as failed when failure fault is uncountered', () => {
    const nodes = computeNodes(baseNodes, [nodeCrashFault], []);
    const apiNode = nodes.find((n) => n.id === 'api');
    expect(apiNode?.status).toBe('failed');
  });

  it('mitigates failure fault to degraded when countered by an active fix', () => {
    const nodes = computeNodes(baseNodes, [nodeCrashFault], [circuitBreakerFix]);
    const apiNode = nodes.find((n) => n.id === 'api');
    expect(apiNode?.status).toBe('degraded');
  });

  it('marks node as degraded when degraded fault is uncountered', () => {
    const nodes = computeNodes(baseNodes, [cacheMissFault], []);
    const cacheNode = nodes.find((n) => n.id === 'cache');
    expect(cacheNode?.status).toBe('degraded');
  });

  it('restores degraded node to healthy when countered by an active fix', () => {
    const nodes = computeNodes(baseNodes, [cacheMissFault], [cacheWarmupFix]);
    const cacheNode = nodes.find((n) => n.id === 'cache');
    expect(cacheNode?.status).toBe('healthy');
  });
});

describe('computeEdges', () => {
  const baseEdges = [dummyEdge('e1'), dummyEdge('e2'), dummyEdge('e3')];

  it('leaves edges normal when no faults are active', () => {
    const edges = computeEdges(baseEdges, [], []);
    expect(edges.find((e) => e.id === 'e1')?.style).toBe('normal');
  });

  it('marks edge as broken when packet loss is uncountered', () => {
    const edges = computeEdges(baseEdges, [packetLossFault], []);
    const e1 = edges.find((e) => e.id === 'e1');
    expect(e1?.style).toBe('broken');
    expect(e1?.animated).toBe(true);
  });

  it('mitigates broken edge to slow when packet loss is countered by retries', () => {
    const edges = computeEdges(baseEdges, [packetLossFault], [retriesFix]);
    const e1 = edges.find((e) => e.id === 'e1');
    expect(e1?.style).toBe('slow');
    expect(e1?.animated).toBe(true);
  });

  it('marks edge as slow when latency spike fault is active', () => {
    const edges = computeEdges(baseEdges, [latencySpikeFault], []);
    const e2 = edges.find((e) => e.id === 'e2');
    expect(e2?.style).toBe('slow');
  });
});

describe('sumMetrics', () => {
  const base: ChaosMetrics = {
    availability: 99.5,
    latency: 100,
    errorRate: 0.5,
    throughput: 1000,
  };

  it('correctly aggregates deltas and clamps boundaries', () => {
    const deltas = [
      { availability: -105, latency: 6000, errorRate: 150, throughput: -2000 },
    ];
    const result = sumMetrics(base, deltas);
    expect(result.availability).toBe(0);
    expect(result.latency).toBe(5000);
    expect(result.errorRate).toBe(100);
    expect(result.throughput).toBe(0);
  });

  it('applies positive and negative deltas accurately', () => {
    const deltas = [
      { availability: -4, latency: 120, errorRate: 2, throughput: -200 },
      { availability: 1.5, latency: -50, errorRate: -1, throughput: 100 },
    ];
    const result = sumMetrics(base, deltas);
    expect(result.availability).toBe(97);
    expect(result.latency).toBe(170);
    expect(result.errorRate).toBe(1.5);
    expect(result.throughput).toBe(900);
  });
});
