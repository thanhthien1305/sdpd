# Translations for Cases 22 to 28
DATA = {
    'case-22': {
        'rootCause': {
            'question': 'Tại sao việc mất một phân mảnh (Shard 7) lại khiến toàn bộ cổng thông tin tư pháp bị tê liệt không thể tra cứu?',
            'options': {
                'rc-4': {
                    'text': 'Bộ định tuyến phân mảnh (Shard Router) bị lỗi phần mềm và tự ý dừng hoạt động khi một shard biến mất',
                    'feedback': 'Bộ định tuyến vẫn hoạt động bình thường, nhưng các truy vấn không có shard key buộc phải quét toàn bộ các shard (Scatter-Gather). Khi một shard không phản hồi, toàn bộ truy vấn bị treo.'
                },
                'rc-1': {
                    'text': 'Dữ liệu của toàn bộ sở cảnh sát đều tập trung trên Shard 7',
                    'feedback': 'Shard 7 chỉ chứa khoảng 12.5% dữ liệu của sở cảnh sát. Vấn đề là kiến trúc phân mảnh không có bản sao dự phòng.'
                },
                'rc-2': {
                    'text': 'Các phân mảnh không có Bản Sao Dự Phòng (No Shard Replicas) — mỗi phân mảnh là một điểm lỗi đơn lẻ độc lập, khiến việc mất 1 shard đồng nghĩa với mất vĩnh viễn quyền truy cập vào phần dữ liệu đó',
                    'feedback': 'Chính xác! Sharding chia dữ liệu theo chiều ngang để mở rộng quy mô, nhưng nếu mỗi Shard chỉ là một máy chủ đơn lẻ không có bản sao (Replication Group), thì xác suất cả hệ thống bị gián đoạn sẽ TĂNG LÊN theo số lượng Shard. Mất Shard 7 khiến 1/8 số vụ án bị biến mất và mọi truy vấn tổng hợp trên toàn thành phố bị lỗi.'
                },
                'rc-3': {
                    'text': 'Mạng nội bộ của trung tâm dữ liệu bị đứt cáp quang kết nối tới Shard 7',
                    'feedback': 'Máy chủ Shard 7 bị chết nguồn và hỏng bo mạch chủ, không phải lỗi cáp mạng.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để ngăn chặn việc mất một Shard làm sập hệ thống tra cứu là gì?',
            'options': {
                'fix-1': {
                    'text': 'Bỏ sharding hoàn toàn và gộp toàn bộ dữ liệu trở lại một cơ sở dữ liệu khổng lồ',
                    'feedback': 'Bỏ sharding khiến hệ thống quay lại với các điểm nghẽn hiệu năng và giới hạn dung lượng lưu trữ của máy chủ đơn lẻ.'
                },
                'fix-2': {
                    'text': 'Cấu hình mỗi Shard thành một Nhóm Bản Sao (Replica Set) — duy trì ít nhất 1 Leader và 2 Follower cho từng phân mảnh với cơ chế tự động chuyển đổi dự phòng (Automatic Failover)',
                    'feedback': 'Chính xác! Nguyên tắc vàng trong kiến trúc phân tán là: "Sharding để mở rộng, Replication để dự phòng". Bằng cách biến mỗi Shard thành một Replica Set (ví dụ sử dụng Raft/Paxos hoặc Leader-Follower), khi máy chủ Shard 7 chính bị cháy bo mạch, bản sao của nó sẽ được thăng cấp lên làm Leader mới trong vài giây, hệ thống không bao giờ bị gián đoạn!'
                },
                'fix-3': {
                    'text': 'In toàn bộ hồ sơ vụ án của Shard 7 ra giấy và cất trong tủ lưu trữ văn phòng',
                    'feedback': 'Hồ sơ giấy không thể tra cứu tự động qua API và không phải là giải pháp kỹ thuật cho hệ thống phần mềm.'
                },
                'fix-4': {
                    'text': 'Bỏ qua các bản ghi thuộc Shard 7 và chỉ trả về kết quả từ các shard còn sống',
                    'feedback': 'Trả về kết quả thiếu mà không có cảnh báo có thể khiến các thẩm phán đưa ra phán quyết sai lầm nghiêm trọng.'
                }
            }
        }
    },
    'case-23': {
        'rootCause': {
            'question': 'Tại sao hai đồn cảnh sát lại nhìn thấy thông tin nhân dạng nghi phạm khác nhau tại cùng một thời điểm?',
            'options': {
                'rc-4': {
                    'text': 'Sĩ quan tại Đồn 1 đã sửa nhầm ảnh nghi phạm mà không lưu lại',
                    'feedback': 'Sĩ quan đã lưu thành công và nhận được xác nhận từ nút cơ sở dữ liệu cục bộ.'
                },
                'rc-1': {
                    'text': 'Một đường truyền mạng bị đứt khiến Đồn 2 hoàn toàn không thể kết nối tới cơ sở dữ liệu',
                    'feedback': 'Đồn 2 vẫn đang đọc dữ liệu từ nút cơ sở dữ liệu cục bộ của họ một cách bình thường.'
                },
                'rc-2': {
                    'text': 'Hệ thống cơ sở dữ liệu phân tán hoạt động ở chế độ Nhất Quán Cuối Cùng (Eventual Consistency) — chấp nhận độ trễ sao chép bất đồng bộ giữa các vùng, khiến các đồn đọc phải dữ liệu cũ chưa đồng bộ',
                    'feedback': 'Chính xác! Để đạt được tính sẵn sàng cao và độ trễ đọc/ghi cực thấp trên diện rộng, hệ thống được cấu hình theo mô hình AP (Available/Partition-tolerant) với tính nhất quán cuối cùng. Khi Đồn 1 cập nhật ảnh nhận dạng mới, thay đổi chỉ mới được ghi vào cụm cục bộ và đang trên đường truyền bất đồng bộ sang Đồn 2. Trong khoảng thời gian trễ đó, Đồn 2 vẫn nhìn thấy ảnh cũ của người vô tội.'
                },
                'rc-3': {
                    'text': 'Cơ sở dữ liệu tại Đồn 2 bị lỗi phần mềm từ chối cập nhật bản ghi mới',
                    'feedback': 'Nút tại Đồn 2 hoạt động bình thường, nó chỉ đơn giản là chưa nhận được gói tin nhân bản từ Đồn 1.'
                }
            }
        },
        'fix': {
            'question': 'Phương pháp tốt nhất để ngăn chặn việc bắt giữ nhầm người do dữ liệu nhận dạng không đồng nhất là gì?',
            'options': {
                'fix-1': {
                    'text': 'Chuyển toàn bộ hệ thống sang mô hình nhân bản đồng bộ hoàn toàn giữa tất cả các đồn cảnh sát trên toàn quốc',
                    'feedback': 'Nhân bản đồng bộ toàn cầu sẽ khiến mọi thao tác ghi bị chậm đi hàng trăm mili-giây và nếu một đồn bị mất mạng, cả thành phố không ai ghi được dữ liệu.'
                },
                'fix-2': {
                    'text': 'Áp dụng chế độ Nhất Quán Mạnh (Strong Consistency / Linearizability) hoặc Đọc Có Túc Số (Quorum Reads: R + W > N) cho các thao tác đọc nhạy cảm liên quan đến nhận dạng nghi phạm',
                    'feedback': 'Chính xác! Đối với các dữ liệu an toàn sinh mạng như nhân dạng nghi phạm đang bị truy bắt, bạn không thể dùng Eventual Consistency. Bằng cách thực thi Quorum Reads (đảm bảo số nút đọc R cộng số nút ghi W lớn hơn tổng số bản sao N) hoặc bắt buộc đọc có kiểm tra phiên bản mới nhất, Đồn 2 sẽ luôn nhận được dữ liệu đã cam kết mới nhất trước khi ra lệnh nổ súng hoặc bắt giữ.'
                },
                'fix-3': {
                    'text': 'Yêu cầu các sĩ quan chụp ảnh nghi phạm bằng máy ảnh chụp lấy ngay polaroid',
                    'feedback': 'Ảnh chụp phim không thể truyền tải và đồng bộ trên hệ thống dữ liệu số hóa toàn thành phố.'
                },
                'fix-4': {
                    'text': 'Chỉ cho phép cập nhật thông tin nhận dạng một lần duy nhất vào lúc nửa đêm',
                    'feedback': 'Thông tin nhận dạng tội phạm nguy hiểm cần cập nhật từng phút khi có manh mối mới.'
                }
            }
        }
    },
    'case-24': {
        'rootCause': {
            'question': 'Tệp video bằng chứng đã bị hỏng ở vị trí nào và tại sao hệ thống không phát hiện ra sự cố?',
            'options': {
                'rc-4': {
                    'text': 'Máy quay bodycam của cảnh sát đã ghi lại tệp video bị lỗi ngay từ ban đầu',
                    'feedback': 'Video gốc trên máy quay hoàn toàn sắc nét và đã được xem trực tiếp tại hiện trường.'
                },
                'rc-1': {
                    'text': 'Đường truyền mạng internet công cộng đã làm mất gói tin khi tải tệp lên máy chủ',
                    'feedback': 'Giao thức TCP đảm bảo truyền tải đầy đủ các gói tin; tệp đã đến máy chủ lưu trữ trọn vẹn lúc tải lên.'
                },
                'rc-2': {
                    'text': 'Hiện Tượng Thối Dữ Liệu Âm Thầm (Silent Bit Rot / Data Corruption) trên đĩa cứng lưu trữ vật lý kết hợp với việc thiếu Cơ Chế Kiểm Tra Mã Băm Toàn Vẹn (Checksum / Hash Verification)',
                    'feedback': 'Chính xác! Sau 2 năm lưu trữ trên các phiến đĩa từ, hiện tượng suy hao từ tính tự nhiên (bit rot) đã làm đảo ngược một số bit trong tệp video. Vì hệ thống lưu trữ không tạo và lưu trữ mã băm kiểm tra tính toàn vẹn (như SHA-256 Checksum) lúc tải lên, nó không hề hay biết tệp đã bị hư hỏng cho đến khi mở ra tại phiên tòa.'
                },
                'rc-3': {
                    'text': 'Phần mềm xem video tại tòa án bị lỗi không hỗ trợ codec của tệp bằng chứng',
                    'feedback': 'Codec hoàn toàn tương thích; các khối dữ liệu nhị phân bên trong tệp thực sự đã bị thay đổi và hỏng cấu trúc.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để ngăn chặn và phát hiện sớm hiện tượng hỏng dữ liệu bằng chứng là gì?',
            'options': {
                'fix-3': {
                    'text': 'Lưu trữ tất cả các video bằng chứng vào thẻ nhớ USB và cất trong két sắt cơ mật',
                    'feedback': 'Bộ nhớ flash NAND trong thẻ USB có tuổi thọ lưu giữ dữ liệu khi không cắm điện còn ngắn hơn cả đĩa cứng từ.'
                },
                'fix-1': {
                    'text': 'Tính toán và lưu trữ Mã Băm Toàn Vẹn (Cryptographic Checksum như SHA-256) ngay khi tải lên, kết hợp Hệ Thống Tự Quét và Tự Sửa Lỗi Định Kỳ (Background Scrubbing & Erasure Coding)',
                    'feedback': 'Chính xác! Bằng cách ghi nhận mã SHA-256 lúc tiếp nhận bằng chứng, hệ thống có thể xác minh tính toàn vẹn bất kỳ lúc nào. Kết hợp với hệ thống tệp tự phục hồi (như ZFS hoặc lưu trữ đám mây dùng Erasure Coding) chạy quét định kỳ (scrubbing), hệ thống sẽ tự động phát hiện các bit bị hỏng và tái tạo lại dữ liệu gốc từ các khối dự phòng trước khi quá muộn.'
                },
                'fix-2': {
                    'text': 'Nén video xuống dung lượng nhỏ nhất có thể để giảm xác suất bị lỗi bit',
                    'feedback': 'Nén dữ liệu làm giảm chất lượng bằng chứng và nếu tệp nén bị lỗi 1 bit, toàn bộ tệp nén sẽ bị hỏng hoàn toàn không thể giải nén.'
                },
                'fix-4': {
                    'text': 'Chỉ xem video bằng chứng trực tiếp trên máy quay và không bao giờ lưu trữ trên máy chủ',
                    'feedback': 'Không thể giữ hàng ngàn máy quay bodycam trong kho lưu trữ bằng chứng của tòa án.'
                }
            }
        }
    },
    'case-25': {
        'rootCause': {
            'question': 'Tại sao hệ thống lưu trữ chỉ chứa 8 TB dữ liệu thực tế nhưng lại tiêu tốn tới 48 TB dung lượng đĩa và gây bão I/O?',
            'options': {
                'rc-3': {
                    'text': 'Hệ điều hành máy chủ bị nhiễm mã độc tự động nhân bản dữ liệu rác vào ổ đĩa',
                    'feedback': 'Không có mã độc nào; toàn bộ dữ liệu đều thuộc cơ sở dữ liệu nhật ký camera giám sát.'
                },
                'rc-1': {
                    'text': 'Cơ chế nén dữ liệu của cơ sở dữ liệu bị hỏng khiến kích thước dữ liệu bị phình to gấp 6 lần',
                    'feedback': 'Thuật toán nén vẫn hoạt động bình thường trên từng khối dữ liệu.'
                },
                'rc-2': {
                    'text': 'Hiện Tượng Khuếch Đại Ghi Quá Mức (Excessive Write Amplification) do quá trình Gom và Hợp Nhất (Compaction) của Cây LSM (Log-Structured Merge-tree) bị quá tải khi dữ liệu ghi liên tục',
                    'feedback': 'Chính xác! Cây LSM tối ưu cho thao tác ghi nhanh bằng cách ghi vào MemTable rồi xả tuần tự xuống các tầng SSTable trên đĩa. Tuy nhiên, khi dữ liệu ghi liên tục với tốc độ cao, quá trình Compaction (đọc các tầng cũ, hợp nhất, sắp xếp và ghi lại ra tầng mới) phải chạy không ngừng nghỉ. Một byte dữ liệu được ghi đi ghi lại trên đĩa tới 6 lần (Write Amplification Factor = 6), gây nghẽn toàn bộ băng thông I/O đĩa cứng.'
                },
                'rc-4': {
                    'text': 'Quản trị viên đã vô tình kích hoạt chế độ sao lưu 6 bản copy trên cùng một ổ đĩa',
                    'feedback': 'Cơ sở dữ liệu chỉ được cấu hình 1 bản lưu duy nhất; dung lượng đĩa bị phình to do các tệp SSTable trung gian chưa kịp dọn dẹp trong quá trình Compaction.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để giảm thiểu hiện tượng khuếch đại ghi và giải phóng I/O cho hệ thống lưu trữ LSM là gì?',
            'options': {
                'fix-1': {
                    'text': 'Chuyển sang công cụ lưu trữ sử dụng B-tree truyền thống cho toàn bộ khối lượng dữ liệu ghi camera khổng lồ',
                    'feedback': 'B-tree thực hiện ghi ngẫu nhiên (random I/O) trực tiếp xuống các trang đĩa, với khối lượng ghi camera khổng lồ thì B-tree sẽ bị nghẽn đĩa còn nhanh hơn nhiều so với LSM.'
                },
                'fix-2': {
                    'text': 'Tinh chỉnh chiến lược Compaction (chuyển sang Leveled hoặc Tiered Compaction phù hợp), tăng kích thước MemTable và phân tầng lưu trữ (đẩy dữ liệu cũ sang kho lưu trữ đối tượng giá rẻ như S3)',
                    'feedback': 'Chính xác! Bằng cách tinh chỉnh chiến lược Compaction (ví dụ Size-Tiered Compaction tối ưu cho khối lượng ghi lớn), tăng dung lượng MemTable trong RAM để xả các khối SSTable lớn hơn, và tự động di chuyển các tệp SSTable cũ đã đóng băng sang Blob Storage giá rẻ, hệ thống sẽ cắt giảm đáng kể số chu kỳ ghi đĩa lặp lại, đưa Write Amplification về mức tối thiểu.'
                },
                'fix-3': {
                    'text': 'Quay lại sử dụng băng từ từ tính thế hệ cũ để lưu trữ toàn bộ dữ liệu nhật ký camera',
                    'feedback': 'Băng từ có độ trễ truy xuất ngẫu nhiên cực lớn (mất nhiều phút để cuộn băng) và không thể phục vụ tra cứu biển số xe theo thời gian thực.'
                },
                'fix-4': {
                    'text': 'Xóa toàn bộ dữ liệu nhật ký camera cũ sau mỗi 24 giờ hoạt động',
                    'feedback': 'Quy định pháp lý yêu cầu lưu trữ dữ liệu camera giám sát giao thông tối thiểu 90 ngày phục vụ điều tra án.'
                }
            }
        }
    },
    'case-26': {
        'rootCause': {
            'question': 'Tại sao một dịch vụ giám định pháp y chạy chậm lại có thể kéo sập toàn bộ Cổng API trung tâm của sở cảnh sát?',
            'options': {
                'rc-4': {
                    'text': 'Dịch vụ giám định pháp y bị tấn công từ chối dịch vụ (DDoS) làm lây lan sang Cổng API',
                    'feedback': 'Lưu lượng hoàn toàn bình thường; dịch vụ chỉ đơn giản là bị chậm do một tác vụ phân tích nặng.'
                },
                'rc-1': {
                    'text': 'Cổng API có lỗi tràn số nguyên trong mã nguồn xử lý định tuyến',
                    'feedback': 'Mã nguồn định tuyến không có lỗi; các luồng xử lý bị đóng băng vì chờ phản hồi từ dịch vụ phụ trợ.'
                },
                'rc-2': {
                    'text': 'Bẫy Thời Gian Chờ (The Timeout Trap / Cascading Thread Exhaustion) — Cổng API có thời gian chờ (timeout) quá dài mà không có cơ chế Ngắt Mạch (Circuit Breaker), khiến toàn bộ luồng xử lý (worker threads) bị chiếm giữ vô hạn',
                    'feedback': 'Chính xác! Khi dịch vụ Giám định pháp y bị chậm do xử lý tác vụ nặng, Cổng API vẫn tiếp tục nhận các yêu cầu mới và cấu hình timeout tới 60 giây. Từng luồng xử lý (thread) trong Thread Pool của Gateway lần lượt bị khóa cứng để chờ phản hồi từ dịch vụ pháp y. Trong vài phút, toàn bộ 500 luồng của Gateway bị cạn kiệt, khiến ngay cả các yêu cầu gọi sang dịch vụ Tuần tra hay Điều phối cũng bị từ chối!'
                },
                'rc-3': {
                    'text': 'Bộ cân bằng tải đã ngừng phân phối lưu lượng tới Cổng API',
                    'feedback': 'Bộ cân bằng tải vẫn gửi lưu lượng đến, nhưng Gateway không còn luồng rảnh để tiếp nhận yêu cầu mới.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để ngăn chặn một dịch vụ chậm làm cạn kiệt tài nguyên của toàn bộ hệ thống là gì?',
            'options': {
                'fix-1': {
                    'text': 'Tăng thời gian timeout của Cổng API lên 10 phút cho mỗi yêu cầu để không bị lỗi timeout',
                    'feedback': 'Tăng timeout lên 10 phút chỉ làm các luồng xử lý bị chiếm giữ lâu hơn gấp 10 lần, khiến Gateway sập nhanh hơn nữa.'
                },
                'fix-2': {
                    'text': 'Cấu hình Thời Gian Chờ Ngắn Chặt Chẽ (Tight Timeouts), áp dụng Lan Truyền Thời Hạn (Deadline Propagation) và triển khai Bộ Ngắt Mạch (Circuit Breaker) kết hợp Vách Ngăn (Bulkheading)',
                    'feedback': 'Chính xác! Ba biện pháp phòng thủ hoàn hảo: (1) Tight Timeouts & Deadline: Giảm timeout xuống mức hợp lý (ví dụ 3s) và truyền deadline xuyên suốt chuỗi vi dịch vụ; (2) Bulkheading: Phân chia thread pool riêng biệt cho từng dịch vụ phụ trợ để sự cố của dịch vụ pháp y không thể ăn vào tài nguyên của dịch vụ điều phối; (3) Circuit Breaker: Tự động ngắt kết nối khi phát hiện dịch vụ bị chậm liên tục, trả về phản hồi fallback tức thì.'
                },
                'fix-3': {
                    'text': 'Cấm dịch vụ pháp y không bao giờ được chạy tác vụ phân tích nặng trên máy chủ',
                    'feedback': 'Tác vụ phân tích pháp y là nghiệp vụ bắt buộc. Hệ thống phải có khả năng cô lập các tác vụ nặng mà không làm ảnh hưởng các dịch vụ khác.'
                },
                'fix-4': {
                    'text': 'Khởi động lại Cổng API định kỳ mỗi 5 phút một lần để giải phóng luồng',
                    'feedback': 'Khởi động lại liên tục sẽ làm rớt kết nối của hàng ngàn sĩ quan đang thao tác và gây gián đoạn dịch vụ liên tục.'
                }
            }
        }
    },
    'case-27': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ khiến Dịch vụ Hồ sơ bị bão hòa và sụp đổ hoàn toàn trong đợt bảo trì là gì?',
            'options': {
                'rc-4': {
                    'text': 'Quá nhiều xe tuần tra hoạt động cùng một lúc vượt quá sức chứa tổng thể của hệ thống',
                    'feedback': '200 xe tuần tra với 600 yêu cầu/phút là mức tải hoàn toàn bình thường mà hệ thống vẫn xử lý hàng ngày.'
                },
                'rc-1': {
                    'text': 'Tác vụ bảo trì cơ sở dữ liệu làm hỏng dữ liệu trong kho lưu trữ của Dịch vụ Hồ sơ',
                    'feedback': 'Tác vụ bảo trì chỉ là việc đánh lại chỉ mục định kỳ và chỉ làm độ trễ tăng nhẹ từ 200ms lên 800ms. Dữ liệu không hề bị hỏng.'
                },
                'rc-2': {
                    'text': 'Cơn Bão Thử Lại (Retry Storm) — các ứng dụng client gửi lại yêu cầu ngay lập tức một cách hung hãn mà không có thời gian chờ, khuếch đại một đợt chậm nhẹ thành một trận quá tải thảm khốc',
                    'feedback': 'Chính xác! Khi Dịch vụ Hồ sơ chỉ bị chậm nhẹ (độ trễ tăng lên 800ms do bảo trì chỉ mục), các ứng dụng trên 200 xe tuần tra bị timeout ở mức 500ms và ngay lập tức bắn 5 yêu cầu thử lại liên tiếp không nghỉ. Lưu lượng bị nhân lên gấp 5-10 lần, biến 600 req/phút thành hơn 3.000 req/phút. Các yêu cầu thử lại mới tiếp tục bị timeout và sinh thêm các lượt thử lại mới, tạo thành vòng xoáy tự hủy diệt dịch vụ!'
                },
                'rc-3': {
                    'text': 'Cổng API Gateway bị tràn bộ nhớ RAM và bị sập do số lượng kết nối quá lớn',
                    'feedback': 'Gateway chỉ là nạn nhân gánh chịu lưu lượng; nguyên nhân cốt lõi là hành vi thử lại điên cuồng từ phía các máy khách.'
                }
            }
        },
        'fix': {
            'question': 'Chiến lược tốt nhất để ngăn chặn hiện tượng Bão Thử Lại (Retry Storm) trong mạng phân tán là gì?',
            'options': {
                'fix-3': {
                    'text': 'Tăng số lượng luồng (thread pool) của Dịch vụ Hồ sơ từ 200 lên 2.000 luồng',
                    'feedback': 'Thêm luồng chỉ trì hoãn cú sập vài chục giây vì bão thử lại tăng trưởng theo cấp số nhân. Bạn phải chặn đứng hành vi thử lại sai lầm.'
                },
                'fix-4': {
                    'text': 'Thêm bộ cân bằng tải và mở rộng thêm nhiều máy chủ Dịch vụ Hồ sơ',
                    'feedback': 'Mở rộng quy mô máy chủ không giải quyết được vòng lặp phản hồi tích cực của bão thử lại; dung lượng càng nhiều thì số lượng request retry sinh ra càng khủng khiếp.'
                },
                'fix-1': {
                    'text': 'Tắt hoàn toàn cơ chế thử lại (Retry) trên tất cả các ứng dụng client',
                    'feedback': 'Tắt hoàn toàn retry sẽ khiến các lỗi mạng chập chờn nhất thời trở thành lỗi vĩnh viễn đối với người dùng. Thử lại là cần thiết, nhưng phải là thử lại thông minh.'
                },
                'fix-2': {
                    'text': 'Triển khai Thuật Toán Thử Lại Lũy Tiến Kèm Dao Động Ngẫu Nhiên (Exponential Backoff with Jitter), giới hạn số lần thử lại tối đa và sử dụng Ngân Sách Thử Lại (Retry Budget)',
                    'feedback': 'Chính xác! Exponential Backoff (chờ 1s, rồi 2s, 4s, 8s...) giúp giãn cách các lần gọi lại. Thêm Jitter (độ lệch ngẫu nhiên) giúp phá vỡ các đợt sóng thử lại đồng loạt của hàng trăm xe cùng lúc. Kết hợp với giới hạn số lần thử (tối đa 3 lần) và Ngân sách thử lại tại Gateway (chỉ cho phép tối đa 10% lưu lượng là retry), hệ thống sẽ cho phép dịch vụ phụ trợ có không gian để tự hồi phục mà không bị đè bẹp.'
                }
            }
        }
    },
    'case-28': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ khiến toàn bộ hệ thống tiếp nhận khẩn cấp 911 bị sập dây chuyền là gì?',
            'options': {
                'rc-1': {
                    'text': 'Đội bảo trì đã tắt dịch vụ Xác Thực Địa Chỉ mà không thông báo trước cho các bộ phận',
                    'feedback': 'Việc bảo trì đã được lên lịch. Trong hệ thống phân tán, các dịch vụ phụ trợ có thể sập bất kỳ lúc nào; kiến trúc hệ thống phải được thiết kế để chịu được việc một dịch vụ ngừng hoạt động.'
                },
                'rc-3': {
                    'text': 'Thời gian chờ 30 giây cấu hình cho cuộc gọi Xác Thực Địa Chỉ là quá dài',
                    'feedback': 'Timeout ngắn hơn giúp giải phóng luồng nhanh hơn, nhưng nếu không có Circuit Breaker thì với hàng nghìn cuộc gọi đến, thread pool vẫn sẽ bị lấp đầy hoàn toàn.'
                },
                'rc-4': {
                    'text': 'Dịch vụ Điều Phối có thread pool quá nhỏ không đủ xử lý giờ cao điểm',
                    'feedback': 'Dù có cấp 1.000 luồng thì khi tất cả các luồng đều bị giữ chân 30 giây trên một dịch vụ đã chết, toàn bộ 1.000 luồng đó cũng sẽ nhanh chóng bị cạn kiệt.'
                },
                'rc-2': {
                    'text': 'Dịch vụ Điều Phối Thiếu Bộ Ngắt Mạch (No Circuit Breaker) — nó tiếp tục khóa cứng toàn bộ luồng xử lý để chờ đợi một dịch vụ đã chết, gây ra Sự Cố Sập Lan Truyền Dây Chuyền (Cascading Failure)',
                    'feedback': 'Chính xác! Khi dịch vụ Xác thực địa chỉ bị tắt để bảo trì, Dịch vụ Điều phối không hề biết và vẫn kiên nhẫn gọi sang với timeout 30 giây cho mỗi yêu cầu. Toàn bộ các luồng của nó bị khóa cứng trong vô vọng. Hậu quả là Dịch vụ Điều phối trở nên bất động, kéo theo Dịch vụ Định tuyến cuộc gọi và Dịch vụ Phân công tuần tra cũng sập theo như hiệu ứng domino!'
                }
            }
        },
        'fix': {
            'question': 'Phương pháp tốt nhất để ngăn chặn sự cố sụp đổ lan truyền dây chuyền giữa các vi dịch vụ là gì?',
            'options': {
                'fix-3': {
                    'text': 'Loại bỏ hoàn toàn sự phụ thuộc vào dịch vụ Xác Thực Địa Chỉ bằng cách nhúng thẳng dữ liệu địa chỉ vào cơ sở dữ liệu của Dịch vụ Điều Phối',
                    'feedback': 'Nhúng toàn bộ dữ liệu vi phạm nguyên tắc phân rã vi dịch vụ và không giải quyết được vấn đề nếu một dịch vụ phụ thuộc khác gặp sự cố.'
                },
                'fix-2': {
                    'text': 'Triển khai dịch vụ Xác Thực Địa Chỉ ở chế độ sẵn sàng cao tuyệt đối không bao giờ được phép tắt',
                    'feedback': 'Không có hệ thống nào cam kết không bao giờ lỗi 100%. Phần mềm vẫn có thể bị sập do bug, cạn tài nguyên hoặc sự cố mạng. Hệ thống luôn phải có cơ chế phòng vệ chủ động.'
                },
                'fix-1': {
                    'text': 'Triển khai Bộ Ngắt Mạch (Circuit Breaker) — tự động ngắt kết nối (Open) khi phát hiện lỗi liên tiếp, lập tức trả về phản hồi dự phòng (Fallback) hoặc báo lỗi nhanh mà không khóa luồng',
                    'feedback': 'Chính xác! Circuit Breaker theo dõi tỷ lệ lỗi của dịch vụ phụ thuộc. Khi thấy lỗi liên tiếp (ví dụ 5 lần trong 10 giây), nó lập tức "ngắt mạch" (chuyển sang trạng thái Open). Tất cả các yêu cầu tiếp theo sẽ không gọi sang dịch vụ đã chết nữa mà lập tức chuyển sang chế độ dự phòng (fallback) — ví dụ tiếp tục điều động xe dựa trên địa chỉ thô chưa qua xác thực. Các luồng được giải phóng ngay lập tức, bảo vệ toàn bộ phần còn lại của hệ sinh thái 911 sống sót an toàn!'
                },
                'fix-4': {
                    'text': 'Bổ sung hàng đợi tin nhắn giữa tất cả các dịch vụ để giao tiếp bất đồng bộ',
                    'feedback': 'Tổng đài 911 tiếp nhận cuộc gọi khẩn cấp yêu cầu phản hồi điều động xe tức thời trong vài giây, không thể chuyển sang xử lý lô qua hàng đợi.'
                }
            }
        }
    }
}
