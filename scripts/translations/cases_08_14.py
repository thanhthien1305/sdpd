# Translations for Cases 08 to 14
DATA = {
    'case-08': {
        'rootCause': {
            'question': 'Nút 3 đang biểu hiện dạng lỗi phân tán nào?',
            'options': {
                'rc-1': {
                    'text': 'Lỗi sập nguồn (Crash fault) — Nút 3 đã dừng xử lý hoàn toàn các yêu cầu gửi tới',
                    'feedback': 'Nút 3 không hề bị chết — nó vẫn đang hoạt động và gửi các phản hồi, nhưng các phản hồi đó lại mâu thuẫn lẫn nhau đối với các nút khác nhau.'
                },
                'rc-3': {
                    'text': 'Lỗi phân vùng mạng — một số thông điệp từ Nút 3 gửi tới các nút khác bị rớt gói tin trên đường truyền',
                    'feedback': 'Hạ tầng mạng truyền tải 100% các gói tin bình thường. Chính Nút 3 đã chủ động tạo ra hai nội dung phân tích khác nhau và gửi đi.'
                },
                'rc-4': {
                    'text': 'Lỗi thuật toán phần mềm bên trong thuật toán so khớp vân tay của Nút 3 tạo ra kết quả ngẫu nhiên',
                    'feedback': 'Dữ liệu cho thấy Nút 3 cố tình gửi kết quả "TRÙNG KHỚP" cho Nút 1 nhưng lại gửi kết quả "KHÔNG TRÙNG KHỚP" cho Nút 2. Đây là hành vi phản trắc có chủ đích hoặc do bị xâm nhập.'
                },
                'rc-2': {
                    'text': 'Lỗi Byzantine (Byzantine Fault) — Nút 3 đã bị xâm nhập hoặc có hành vi gian lận, gửi các thông tin mâu thuẫn trái ngược nhau cho các nút khác trong mạng',
                    'feedback': 'Chính xác! Lỗi Byzantine là dạng lỗi nghiêm trọng nhất trong hệ thống phân tán: một nút không chỉ đơn giản là sập, mà nó có hành vi lừa dối, gửi dữ liệu sai lệch hoặc mâu thuẫn cho các thành viên khác để phá hoại sự đồng thuận. Để chống lại lỗi này, hệ thống cần các thuật toán chịu lỗi Byzantine (BFT).'
                }
            }
        },
        'fix': {
            'question': 'Mạng lưới giám định pháp y cần được thiết kế như thế nào để chống chịu được lỗi Byzantine?',
            'options': {
                'fix-3': {
                    'text': 'Sử dụng cơ chế biểu quyết đa số đơn giản (> 50%) — chấp nhận kết quả nào nhận được nhiều hơn một nửa số phiếu',
                    'feedback': 'Bỏ phiếu đa số thông thường (Crash Fault Tolerant) chỉ hoạt động khi các nút trung thực và chỉ có nguy cơ bị sập. Khi có nút phản trắc nói dối, bỏ phiếu đa số đơn giản sẽ dễ dàng bị thao túng.'
                },
                'fix-2': {
                    'text': 'Yêu cầu sự nhất trí 100% (Unanimous agreement) từ tất cả các nút trong cụm trước khi đưa ra kết luận',
                    'feedback': 'Yêu cầu 100% nhất trí có nghĩa là chỉ cần một nút bị sập hoặc cố tình bỏ phiếu ngược lại, toàn bộ hệ thống sẽ bị tê liệt vĩnh viễn (mất hoàn toàn tính sẵn sàng).'
                },
                'fix-1': {
                    'text': 'Áp dụng giao thức Đồng Thuận Chống Lỗi Byzantine (BFT - Byzantine Fault Tolerant) với yêu cầu tối thiểu 3f + 1 nút để chịu được f nút gian lận (ví dụ cần ít nhất 4 nút để chịu 1 nút phản trắc)',
                    'feedback': 'Chính xác! Theo định lý toán học của PBFT, để chịu được f nút có hành vi Byzantine độc hại, hệ thống cần tối thiểu 3f + 1 nút và yêu cầu túc số 2f + 1 phiếu đồng thuận kèm chữ ký mật mã. Với 4 nút, hệ thống có thể phát hiện và cô lập hoàn toàn 1 nút gian dối như Nút 3 mà vẫn đưa ra kết luận pháp y chính xác.'
                },
                'fix-4': {
                    'text': 'Bổ sung mã hóa đầu-cuối (End-to-end encryption) cho tất cả các kênh liên lạc giữa các nút',
                    'feedback': 'Mã hóa đường truyền bảo vệ dữ liệu khỏi kẻ nghe lén bên ngoài, nhưng không thể ngăn chặn một nút bên trong mạng đã bị chiếm quyền và tự tạo ra dữ liệu dối trá.'
                }
            }
        }
    },
    'case-09': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ gây ra sự cố sập toàn bộ hệ thống trong trận động đất là gì?',
            'options': {
                'rc-4': {
                    'text': 'Trận động đất gây ra thiệt hại vật lý trực tiếp tới phần cứng của các trung tâm dữ liệu',
                    'feedback': 'Tất cả các máy chủ phụ trợ (backend services) đều nguyên vẹn và đang hoạt động tốt. Vấn đề nằm ở cổng tiếp nhận lưu lượng.'
                },
                'rc-1': {
                    'text': 'Bản thân các dịch vụ nghiệp vụ phía sau (Backend Services) không thể chịu được mức tăng đột biến của lưu lượng',
                    'feedback': 'Các dịch vụ phụ trợ phía sau thậm chí còn chưa nhận được yêu cầu nào vì cổng API Gateway đã bị nghẽn cứng ngay từ cửa vào.'
                },
                'rc-2': {
                    'text': 'Một cá thể API Gateway duy nhất là nút thắt cổ chai (Single Bottleneck) — nó không thể mở rộng và bị cạn kiệt tài nguyên khi lưu lượng tăng vọt 15 lần trong tình huống khẩn cấp',
                    'feedback': 'Chính xác! Cổng API Gateway là điểm tiếp xúc đầu tiên của toàn bộ hệ thống. Mặc dù các dịch vụ phía sau được chia nhỏ, việc chỉ đặt một API Gateway duy nhất phía trước mà không có bộ cân bằng tải (Load Balancer) đã tạo ra một điểm nghẽn nghiêm trọng. Khi lưu lượng bùng nổ từ 200 lên 3.000 yêu cầu/giây, gateway cạn kiệt CPU và luồng kết nối, chặn đứng mọi cuộc gọi khẩn cấp.'
                },
                'rc-3': {
                    'text': 'Bão thử lại (Retry Storm) dữ dội từ các đồn cảnh sát đã đánh sập cơ sở dữ liệu',
                    'feedback': 'Bão thử lại là hệ quả xuất hiện sau khi người dùng thấy lỗi kết nối, không phải nguyên nhân ban đầu đánh sập gateway.'
                }
            }
        },
        'fix': {
            'question': 'Phương pháp tốt nhất để ngăn chặn tình trạng quá tải API Gateway khi lưu lượng tăng vọt là gì?',
            'options': {
                'fix-3': {
                    'text': 'Triển khai giới hạn tốc độ (Rate Limiting) trên Gateway để từ chối ngay các yêu cầu vượt ngưỡng',
                    'feedback': 'Trong trận động đất khẩn cấp, việc từ chối các cuộc gọi cứu nạn của người dân và cảnh sát là điều không thể chấp nhận được. Hệ thống cần phải mở rộng để tiếp nhận cuộc gọi, không phải vứt bỏ chúng.'
                },
                'fix-4': {
                    'text': 'Xóa bỏ hoàn toàn tầng API Gateway và để từng đồn cảnh sát kết nối trực tiếp vào từng dịch vụ backend',
                    'feedback': 'Bỏ Gateway làm lộ toàn bộ mạng nội bộ ra ngoài, gây khó khăn cho việc xác thực, định tuyến và phân tán bảo mật.'
                },
                'fix-1': {
                    'text': 'Triển khai nhiều phiên bản API Gateway phía sau một Bộ Cân Bằng Tải (Load Balancer) kết hợp cơ chế Tự Động Co Giãn (Auto-scaling)',
                    'feedback': 'Chính xác! Bằng cách đặt một cụm API Gateway nằm sau Bộ cân bằng tải L4/L7 có tính sẵn sàng cao kết hợp Auto-scaling, khi thảm họa xảy ra và lưu lượng tăng gấp 15 lần, hệ thống sẽ tự động kích hoạt thêm hàng chục instance gateway mới trong vài chục giây để san sẻ tải, đảm bảo không một yêu cầu khẩn cấp nào bị nghẽn.'
                },
                'fix-2': {
                    'text': 'Nâng cấp máy chủ API Gateway duy nhất hiện tại lên một cấu hình phần cứng cực mạnh (Scale Up)',
                    'feedback': 'Mở rộng theo chiều dọc luôn có giới hạn vật lý và chi phí cực kỳ đắt đỏ, đồng thời vẫn giữ nguyên điểm lỗi đơn lẻ (SPOF) nếu máy chủ đó gặp trục trặc.'
                }
            }
        }
    },
    'case-10': {
        'rootCause': {
            'question': 'Điều gì đã khiến cơ sở dữ liệu bị tê liệt chính xác vào lúc 06:00 sáng?',
            'options': {
                'rc-3': {
                    'text': 'Máy chủ Redis gặp lỗi ngoại lệ chưa được xử lý, bị sập và mất toàn bộ dữ liệu trong bộ nhớ RAM',
                    'feedback': 'Máy chủ cache hoạt động hoàn toàn bình thường và không hề bị sập. Dữ liệu trong cache hết hạn một cách hợp lệ theo đúng thời gian sống TTL 24 giờ đã cấu hình.'
                },
                'rc-1': {
                    'text': 'Phần cứng máy chủ cơ sở dữ liệu quá yếu và không đủ năng lực xử lý số lượng truy vấn bắt đầu ca trực lúc 06:00',
                    'feedback': 'Cơ sở dữ liệu xử lý 50 truy vấn/giây với độ trễ 50ms trong điều kiện bình thường rất mượt mà. Vấn đề là 2.400 truy vấn ập đến chỉ trong 1 giây (gấp 48 lần mức tải) do cache hết hạn đồng loạt.'
                },
                'rc-2': {
                    'text': 'Bão Trượt Cache (Cache Stampede / Thundering Herd) — khóa dữ liệu trong cache hết hạn đồng thời cho tất cả người dùng, khiến hàng nghìn yêu cầu cùng lúc ập thẳng xuống cơ sở dữ liệu',
                    'feedback': 'Chính xác! Đây là hiện tượng Cache Stampede kinh điển. Khóa danh sách truy nã được nạp lúc 06:00 hôm trước với TTL tròn 24 giờ. Đúng 06:00 hôm sau, khóa hết hạn. Đúng khoảnh khắc đó, 2.400 sĩ quan đồng loạt đăng nhập vào ca trực, thấy cache rỗng và cùng lúc gửi truy vấn xuống cơ sở dữ liệu để tính toán lại. DB bị quá tải đến mức không kịp phản hồi để nạp lại cache, tạo thành vòng lặp sụp đổ.'
                },
                'rc-4': {
                    'text': 'Việc quá nhiều sĩ quan bắt đầu ca trực cùng lúc 06:00 là một sự bùng nổ bất thường ngoài tầm kiểm soát của hệ thống',
                    'feedback': 'Việc sĩ quan bắt đầu ca lúc 06:00 là hoạt động hoàn toàn định kỳ và dự đoán trước được. Khi có cache hoạt động tốt, chỉ 1 yêu cầu đầu tiên nạp cache và 2.399 người sau sẽ nhận dữ liệu từ RAM trong vài micro-giây.'
                }
            }
        },
        'fix': {
            'question': 'Chiến lược tốt nhất để triệt tiêu hiện tượng Cache Stampede (Thundering Herd) là gì?',
            'options': {
                'fix-1': {
                    'text': 'Mở rộng kích thước bể kết nối (Connection Pool) của cơ sở dữ liệu để đủ sức chứa toàn bộ 2.400 truy vấn đồng thời',
                    'feedback': 'Mở thêm kết nối không giúp ích gì nếu CPU của cơ sở dữ liệu bị bão hòa. Mục tiêu của kiến trúc là ngăn chặn hiện tượng bão trượt xảy ra, chứ không phải cố gắng chịu đòn.'
                },
                'fix-3': {
                    'text': 'Đặt thời gian sống TTL của khóa trong cache thành vô hạn để danh sách không bao giờ hết hạn',
                    'feedback': 'Cache vĩnh viễn sẽ khiến dữ liệu bị cũ (stale) — tội phạm mới bị truy nã sẽ không xuất hiện, người đã được xóa án tích vẫn nằm trên danh sách.'
                },
                'fix-2': {
                    'text': 'Sử dụng Khóa Bộ Nhớ Đệm (Cache Lock / Mutex) để chỉ 1 yêu cầu duy nhất được xuống DB nạp lại cache trong khi các yêu cầu khác kiên nhẫn chờ, kết hợp Dao Động Thời Gian Sống (TTL Jitter)',
                    'feedback': 'Chính xác! Hai kỹ thuật hoàn hảo bổ trợ cho nhau: (1) Cache Mutex / Singleflight: Khi cache hết hạn, chỉ yêu cầu đầu tiên được cấp khóa để xuống DB nạp lại, các yêu cầu khác đứng chờ và dùng chung kết quả mới. 2.400 truy vấn DB được gom lại thành đúng 1 truy vấn! (2) TTL Jitter: Thêm độ lệch ngẫu nhiên vào TTL (ví dụ 24h ± 15 phút) để các khóa không bao giờ hết hạn cùng một giây chính xác.'
                },
                'fix-4': {
                    'text': 'Lập lịch một tác vụ làm ấm cache (Pre-warm) chạy lúc 05:59 hàng ngày để nạp trước dữ liệu',
                    'feedback': 'Làm ấm chỉ áp dụng được cho trường hợp cụ thể này, không giải quyết được các khóa dữ liệu khác có mẫu truy cập ngẫu nhiên. Cache lock và TTL Jitter là giải pháp toàn diện cho mọi bài toán cache.'
                }
            }
        }
    },
    'case-11': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ dẫn đến việc Shard 4 bị quá tải trong khi các Shard khác hoàn toàn rảnh rỗi là gì?',
            'options': {
                'rc-3': {
                    'text': 'Phần cứng của Shard 4 bị suy giảm hiệu năng do lỗi ổ đĩa hoặc bộ nhớ RAM',
                    'feedback': 'Phần cứng của Shard 4 hoàn toàn giống hệt các Shard khác. Nó bị quá tải đơn thuần vì phải hứng chịu tới 70% tổng lưu lượng truy vấn của toàn bộ hệ thống.'
                },
                'rc-1': {
                    'text': 'Bộ cân bằng tải cấp cơ sở dữ liệu gặp lỗi và chuyển nhầm toàn bộ lưu lượng vào Shard 4',
                    'feedback': 'Hệ thống sharding định tuyến theo khóa phân vùng chứ không dùng round-robin ngẫu nhiên. Bộ định tuyến hoạt động đúng theo quy tắc phân mảnh đã cấu hình.'
                },
                'rc-4': {
                    'text': 'Dữ liệu được lưu trữ trên Shard 4 bị phân mảnh nghiêm trọng cần phải thực hiện nén đĩa',
                    'feedback': 'Phân mảnh đĩa không phải là nguyên nhân gây ra sự chênh lệch lưu lượng khổng lồ giữa các shard.'
                },
                'rc-2': {
                    'text': 'Hiện Tượng Phân Vùng Nóng (Hot Partition) do chọn khóa phân mảnh kém — sharding theo Quận (Precinct) khiến quận trung tâm đông đúc dồn toàn bộ dữ liệu vào một máy chủ duy nhất',
                    'feedback': 'Chính xác! Shard 4 chứa dữ liệu của Quận Downtown — nơi tập trung hầu hết các vụ việc và sĩ quan hoạt động. Chọn Khóa Phân Mảnh (Shard Key) có độ phân tán (cardinality) thấp hoặc phân bổ không đồng đều là sai lầm kinh điển. Shard 4 gánh 70% tải trong khi Shard 1, 2, 3 chỉ gánh 10% mỗi shard.'
                }
            }
        },
        'fix': {
            'question': 'Chiến lược phân mảnh dữ liệu nào tốt nhất để phân bổ tải đồng đều trên toàn bộ các Shard?',
            'options': {
                'fix-3': {
                    'text': 'Nâng cấp máy chủ Shard 4 lên một cấu hình phần cứng lớn gấp 5 lần các shard khác',
                    'feedback': 'Đây là giải pháp chắp vá và không bền vững. Khi một quận khác bùng nổ sự kiện, bạn lại phải đoán để nâng cấp shard đó.'
                },
                'fix-1': {
                    'text': 'Sử dụng Phân Mảnh Theo Băm Nhất Quán (Consistent Hashing) trên một khóa có độ phân tán cao (như incident_id) hoặc Khóa Hỗn Hợp (precinct_id + incident_id)',
                    'feedback': 'Chính xác! Bằng cách băm một khóa có độ phân tán cao như incident_id, các vụ việc trong cùng quận Downtown sẽ được rải đều ngẫu nhiên trên toàn bộ các shard. Tất cả các máy chủ sẽ chịu tải đồng đều nhau (~25% mỗi shard), triệt tiêu hoàn toàn hiện tượng phân vùng nóng (hotspot).'
                },
                'fix-2': {
                    'text': 'Chuyển một nửa các đồn cảnh sát thuộc Shard 4 sang Shard 1 một cách thủ công',
                    'feedback': 'Tái cấu hình thủ công rất tốn công và sẽ lại mất cân bằng ngay khi mật độ sự kiện thay đổi. Hệ thống cần cơ chế phân bổ tự động bằng thuật toán băm.'
                },
                'fix-4': {
                    'text': 'Bỏ sharding và gộp toàn bộ dữ liệu trở lại một cơ sở dữ liệu khổng lồ duy nhất',
                    'feedback': 'Quay về cơ sở dữ liệu đơn lẻ sẽ đưa hệ thống quay lại vấn đề Điểm Lỗi Đơn (SPOF) và giới hạn trần dung lượng phần cứng.'
                }
            }
        }
    },
    'case-12': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ của sự cố hệ thống phân tích dữ liệu tội phạm bị chậm nghiêm trọng là gì?',
            'options': {
                'rc-4': {
                    'text': 'Dung lượng lưu trữ đĩa trên máy chủ phân tích đã đạt mức 98% khiến hệ điều hành bị nghẽn I/O',
                    'feedback': 'Đĩa cứng vẫn còn trống nhiều. Nút thắt cổ chai là CPU và RAM liên tục chạm ngưỡng 100% trong quá trình xử lý tính toán.'
                },
                'rc-1': {
                    'text': 'Hệ điều hành của máy chủ gặp lỗi rò rỉ bộ nhớ (Memory Leak) làm cạn kiệt RAM theo thời gian',
                    'feedback': 'Bộ nhớ bị chiếm dụng hoàn toàn bởi các tiến trình tính toán phân tích và tập dữ liệu lớn hợp lệ, không phải do memory leak.'
                },
                'rc-2': {
                    'text': 'Hệ thống đã chạm Giới Hạn Mở Rộng Theo Chiều Dọc (Vertical Limit) — một máy chủ đơn lẻ dù mạnh nhất cũng không thể xử lý khối lượng dữ liệu phân tích đang tăng trưởng theo cấp số nhân',
                    'feedback': 'Chính xác! Sở cảnh sát đã liên tục mở rộng theo chiều dọc (Scale Up) bằng cách nâng cấp CPU và RAM lớn hơn trên một máy chủ duy nhất. Nhưng khối lượng dữ liệu tội phạm và các truy vấn phân tích phức tạp đã vượt quá giới hạn phần cứng vật lý lớn nhất có thể mua được trên thị trường. Đây là trần giới hạn của Scale Up.'
                },
                'rc-3': {
                    'text': 'Các câu truy vấn SQL chạy bảng điều khiển phân tích được tối ưu hóa quá kém và thiếu chỉ mục',
                    'feedback': 'Dù có tối ưu hóa câu lệnh thì khi quy mô dữ liệu đạt tới hàng chục terabyte, một máy chủ đơn lẻ vẫn không thể vừa chạy xử lý hàng loạt vừa phục vụ truy vấn thời gian thực.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để mở rộng hệ thống phân tích tội phạm bền vững trong tương lai là gì?',
            'options': {
                'fix-3': {
                    'text': 'Cắt giảm bớt khối lượng dữ liệu tội phạm cũ được lưu trữ để giảm gánh nặng cho máy chủ',
                    'feedback': 'Xóa dữ liệu lịch sử phá hỏng mục đích cốt lõi của phòng phân tích điều tra (vốn cần dữ liệu nhiều năm để phát hiện quy luật phạm tội).'
                },
                'fix-2': {
                    'text': 'Chờ đợi thế hệ vi xử lý và phần cứng máy chủ tiếp theo ra mắt với nhiều lõi CPU và RAM khủng hơn',
                    'feedback': 'Chờ phần cứng mới chỉ trì hoãn vấn đề tạm thời. Dữ liệu sẽ lại nhanh chóng vượt qua giới hạn của thế hệ phần cứng đó.'
                },
                'fix-1': {
                    'text': 'Chuyển đổi sang kiến trúc Mở Rộng Theo Chiều Ngang (Horizontal Scaling / Scale Out) — phân tán tải xử lý qua nhiều máy chủ phân tích phía sau bộ cân bằng tải hoặc cụm điện toán phân tán',
                    'feedback': 'Chính xác! Mở rộng theo chiều ngang (Scale Out) cho phép bạn bổ sung thêm nhiều máy chủ thương mại tiêu chuẩn vào cụm khi nhu cầu tăng lên. Các tác vụ xử lý lô (batch jobs) và truy vấn thời gian thực có thể phân tán trên các nút tính toán riêng biệt (như cụm Spark hoặc hệ thống OLAP phân tán). Khác với Scale Up, Scale Out không có trần giới hạn phần cứng.'
                },
                'fix-4': {
                    'text': 'Viết lại toàn bộ hệ thống phân tích bằng một ngôn ngữ lập trình cấp thấp hơn như C++ để tối ưu hiệu năng',
                    'feedback': 'Kể cả phần mềm chạy nhanh hơn thì một máy chủ đơn lẻ cũng chỉ có giới hạn 100% tài nguyên nhất định. Vấn đề cốt tử nằm ở kiến trúc máy chủ đơn lẻ.'
                }
            }
        }
    },
    'case-13': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ khiến 340 sĩ quan tuần tra bị đăng xuất đột ngột và mất dữ liệu báo cáo là gì?',
            'options': {
                'rc-1': {
                    'text': 'Bộ cân bằng tải đã không phân phối lại các phiên hoạt động sang các máy chủ còn sống sau khi Máy chủ 2 gặp sự cố',
                    'feedback': 'Bộ cân bằng tải đã định tuyến lại các yêu cầu mới rất chuẩn xác, nhưng dữ liệu phiên đăng nhập chỉ nằm trong bộ nhớ RAM của Máy chủ 2. Dữ liệu phiên đã chết theo máy chủ, không còn gì để chuyển giao.'
                },
                'rc-2': {
                    'text': 'Kiến trúc Phiên Gắn Kết (Sticky Sessions) lưu trạng thái phiên trực tiếp trong bộ nhớ cục bộ của từng máy chủ — khi máy chủ sập, toàn bộ phiên đăng nhập của người dùng trên đó biến mất',
                    'feedback': 'Chính xác! Khi sử dụng Sticky Sessions, trạng thái phiên làm việc của sĩ quan được lưu trực tiếp trong RAM của Máy chủ 2. Điều này biến các máy chủ ứng dụng thành hệ thống có trạng thái (stateful). Khi Máy chủ 2 bị tràn bộ nhớ (OOM) và khởi động lại, toàn bộ 340 phiên làm việc bị xóa sạch. Các sĩ quan bị đá văng ra màn hình đăng nhập và mất trắng dữ liệu báo cáo chưa lưu.'
                },
                'rc-3': {
                    'text': 'Máy chủ 2 bị cạn kiệt bộ nhớ vì nó được giao quá nhiều phiên gắn kết so với các máy chủ khác',
                    'feedback': 'Dù các phiên có được chia đều tuyệt đối thì bất kỳ khi nào một máy chủ gặp sự cố, các phiên nằm trên nó cũng sẽ biến mất nếu lưu trong RAM cục bộ.'
                },
                'rc-4': {
                    'text': 'Các máy chủ ứng dụng thiếu cơ chế sao lưu định kỳ dữ liệu phiên ra đĩa cứng',
                    'feedback': 'Ghi phiên ra đĩa cục bộ không giải quyết được vấn đề khi máy chủ bị sập và các máy chủ khác cần phục vụ tiếp người dùng đó.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để ngăn ngừa việc mất phiên làm việc khi máy chủ ứng dụng gặp sự cố là gì?',
            'options': {
                'fix-4': {
                    'text': 'Thiết lập chính sách tự động khởi động lại máy chủ cực nhanh trước khi các phiên bị hết hạn',
                    'feedback': 'Khi tiến trình bị chết, bộ nhớ RAM bị hệ điều hành thu hồi sạch sẽ. Khởi động lại nhanh thì máy chủ vẫn là một trang giấy trắng.'
                },
                'fix-1': {
                    'text': 'Tăng thêm số lượng máy chủ ứng dụng để mỗi máy chủ chỉ chứa ít phiên hơn, giảm bán kính ảnh hưởng',
                    'feedback': 'Tăng số máy chủ chỉ làm giảm số nạn nhân trong mỗi vụ sập, chứ không ngăn chặn được việc mất phiên và mất dữ liệu của người dùng.'
                },
                'fix-2': {
                    'text': 'Thiết kế ứng dụng Phi Trạng Thái (Stateless Services) — lưu trữ toàn bộ phiên làm việc tại một kho lưu trữ tập trung dùng chung bên ngoài (như cụm Redis Cluster)',
                    'feedback': 'Chính xác! Bằng cách đưa phiên làm việc (session state) ra một kho lưu trữ chuyên dụng bên ngoài như Redis, các máy chủ ứng dụng trở thành hoàn toàn phi trạng thái (stateless). Bất kỳ máy chủ nào trong cụm cũng có thể nhận và xử lý yêu cầu của bất kỳ sĩ quan nào. Khi một máy chủ sập, bộ cân bằng tải chuyển người dùng sang máy khác ngay lập tức mà người dùng không hề nhận ra sự gián đoạn.'
                },
                'fix-3': {
                    'text': 'Sao chép dữ liệu phiên trong bộ nhớ giữa cả ba máy chủ trong thời gian thực bằng cơ chế đồng bộ phiên',
                    'feedback': 'Sao chép bộ nhớ giữa các máy chủ ứng dụng (session replication) cực kỳ tốn băng thông, phức tạp và không thể mở rộng khi số lượng máy chủ tăng lên.'
                }
            }
        }
    },
    'case-14': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ khiến bản ghi án tích đã xóa của Marcus Vance vẫn tiếp tục hiển thị trên màn hình sĩ quan tuần tra là gì?',
            'options': {
                'rc-2': {
                    'text': 'Bộ nhớ đệm (Cache) không bao giờ bị vô hiệu hóa khi bản ghi bị xóa trong cơ sở dữ liệu — nó tiếp tục phục vụ dữ liệu cũ bóng ma cho đến khi hết hạn TTL 30 ngày',
                    'feedback': 'Chính xác! Bộ nhớ đệm Redis được cấu hình TTL 30 ngày nhưng ứng dụng lại không có cơ chế vô hiệu hóa cache khi ghi/xóa (Cache Invalidation on Write). Khi thẩm phán xóa án tích trong MySQL, cơ sở dữ liệu đã sạch, nhưng khóa trong Redis không hề nhận được thông báo. Trong suốt 3 tuần tiếp theo, mọi sĩ quan tra cứu đều nhận dữ liệu bóng ma từ Redis mà không chạm tới DB.'
                },
                'rc-3': {
                    'text': 'Thiết bị của sĩ quan có bộ nhớ đệm cục bộ ngoại tuyến chưa được làm mới kể từ phiên làm việc trước',
                    'feedback': 'Thiết bị sĩ quan gọi API thời gian thực. Dữ liệu ma đến từ chính máy chủ Redis của trung tâm, không phải từ máy cục bộ.'
                },
                'rc-1': {
                    'text': 'Lệnh xóa trong cơ sở dữ liệu thất bại âm thầm và bản ghi vẫn còn tồn tại vật lý trong bảng MySQL',
                    'feedback': 'Nhật ký cơ sở dữ liệu xác nhận lệnh DELETE đã chạy thành công 3 tuần trước. Khi truy vấn trực tiếp vào MySQL, kết quả trả về là rỗng.'
                },
                'rc-4': {
                    'text': 'Độ trễ nhân bản cơ sở dữ liệu khiến việc xóa bản ghi chưa kịp truyền tới các nút bản sao',
                    'feedback': 'Lệnh xóa đã diễn ra từ 3 tuần trước. Độ trễ nhân bản tính bằng giây, không thể kéo dài suốt 3 tuần.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để ngăn chặn các bản ghi bóng ma lỗi thời xuất hiện trong bộ nhớ đệm là gì?',
            'options': {
                'fix-4': {
                    'text': 'Bổ sung một nút bấm "Xóa toàn bộ Cache" thủ công để quản trị viên bấm sau khi thực hiện xóa bản ghi quan trọng',
                    'feedback': 'Quy trình thủ công chắc chắn sẽ bị con người lãng quên và không thể áp dụng ở quy mô hàng ngàn cập nhật mỗi ngày.'
                },
                'fix-1': {
                    'text': 'Hạ thấp thời gian sống TTL của cache từ 30 ngày xuống còn 5 phút',
                    'feedback': 'Giảm TTL giúp giảm khoảng thời gian dữ liệu sai lệch, nhưng trong 5 phút đó, sĩ quan vẫn có thể vi phạm pháp luật vì hành động theo án tích ma. Đối với dữ liệu xóa án tích, tính chính xác phải là tức thì.'
                },
                'fix-2': {
                    'text': 'Thực hiện Vô Hiệu Hóa Cache Khi Ghi (Cache Invalidation on Write / Event-driven Invalidation) — tự động xóa hoặc cập nhật khóa tương ứng trong Redis ngay khi bản ghi trong DB thay đổi',
                    'feedback': 'Chính xác! Khi có thao tác DELETE hoặc UPDATE trong cơ sở dữ liệu, ứng dụng phải lập tức chủ động xóa khóa đó trong Redis (hoặc dùng CDC - Change Data Capture). Khi sĩ quan tra cứu ở giây tiếp theo, cache miss sẽ xảy ra, hệ thống đọc từ cơ sở dữ liệu và thấy không có bản ghi, trả về kết quả chính xác 100% tức thì.'
                },
                'fix-3': {
                    'text': 'Tắt hoàn toàn tầng bộ đệm Redis đối với hồ sơ tội phạm và luôn đọc thẳng từ cơ sở dữ liệu',
                    'feedback': 'Tắt cache sẽ làm tăng tải cho cơ sở dữ liệu lên gấp 16 lần (tỷ lệ trúng cache hiện tại là 94%), dễ dẫn tới sập DB khi cao điểm.'
                }
            }
        }
    }
}
