# Translations for Cases 29 to 33
DATA = {
    'case-29': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ khiến toàn bộ các dịch vụ mất kết nối sau khi chuyển máy chủ là gì?',
            'options': {
                'rc-4': {
                    'text': 'Máy chủ mới được triển khai với hệ điều hành không tương thích',
                    'feedback': 'Máy chủ mới hoạt động hoàn toàn bình thường và đã được kiểm thử trước khi chuyển giao.'
                },
                'rc-1': {
                    'text': 'Tường lửa mạng trung tâm chặn toàn bộ lưu lượng cổng 5432 giữa các dịch vụ',
                    'feedback': 'Quy tắc tường lửa đã được cập nhật cho cả dải IP mạng nội bộ.'
                },
                'rc-2': {
                    'text': 'Máy chủ thay thế lẽ ra phải được gán đúng địa chỉ IP cũ 10.0.1.50 thay vì dùng địa chỉ IP mới',
                    'feedback': 'Gán IP tĩnh cũ có thể giải quyết tạm thời cho lần này, nhưng kiến trúc dựa vào IP cố định (hardcoded IP) là nguyên nhân sâu xa khiến việc nâng cấp hạ tầng luôn dẫn tới thảm họa.'
                },
                'rc-3': {
                    'text': 'Cấu Hình Địa Chỉ IP Tĩnh Cố Định (Hardcoded IP Addresses) mà không có Cơ Chế Khám Phá Dịch Vụ (Service Discovery) — các ứng dụng gọi thẳng vào IP cũ thay vì dùng tên miền hoặc bộ đăng ký dịch vụ',
                    'feedback': 'Chính xác! Tất cả các vi dịch vụ đều ghi cứng địa chỉ IP "10.0.1.50" trong tệp cấu hình của mình. Khi máy chủ cơ sở dữ liệu cũ bị khai tử và thay thế bằng máy chủ mới có IP khác, không một dịch vụ nào có thể tự động tìm thấy máy chủ mới. Việc phụ thuộc vào địa chỉ IP tĩnh cố định trong môi trường đám mây hoặc mạng phân tán là sai lầm chết người!'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp dài hạn tốt nhất để ngăn chặn các sự cố mất kết nối khi nâng cấp hạ tầng mạng là gì?',
            'options': {
                'fix-4': {
                    'text': 'Giữ nguyên máy chủ cũ chạy mãi mãi tại phòng máy của sở cảnh sát và không bao giờ nâng cấp',
                    'feedback': 'Không thể duy trì hạ tầng cũ lỗi thời, thiếu bảo mật và không thể mở rộng dung lượng.'
                },
                'fix-1': {
                    'text': 'Tạo một tệp cấu hình dùng chung duy nhất đặt trên máy chủ tệp mạng liệt kê tất cả các địa chỉ IP',
                    'feedback': 'Một tệp cấu hình tập trung vẫn đòi hỏi phải cập nhật và khởi động lại toàn bộ ứng dụng mỗi khi IP thay đổi.'
                },
                'fix-2': {
                    'text': 'Triển khai Hệ Thống Khám Phá Dịch Vụ (Service Discovery như Consul, Eureka hoặc Kubernetes DNS) — các dịch vụ tự động đăng ký và tìm kiếm nhau thông qua tên miền logic thay vì địa chỉ IP vật lý',
                    'feedback': 'Chính xác! Với hệ thống Khám phá dịch vụ (Service Discovery kết hợp Internal DNS), các dịch vụ chỉ cần kết nối tới tên logic như "db-primary.service.internal". Khi một máy chủ mới được tạo ra (hoặc IP thay đổi), hệ thống tự động cập nhật bản ghi trong bộ đăng ký dịch vụ (Service Registry). Tất cả các dịch vụ gọi đến sẽ tự động được định tuyến tới IP mới mà không cần sửa code hay khởi động lại!'
                },
                'fix-3': {
                    'text': 'Cấu hình để mọi dịch vụ tự động quét toàn bộ dải mạng subnet mỗi khi bị mất kết nối',
                    'feedback': 'Quét mạng liên tục sẽ tạo ra bão lưu lượng broadcast, làm tắc nghẽn switch và gây ra các lỗ hổng bảo mật nghiêm trọng.'
                }
            }
        }
    },
    'case-30': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ khiến cả hai dịch vụ cùng bị treo cứng (bị đóng băng hoàn toàn) là gì?',
            'options': {
                'rc-4': {
                    'text': 'Cơ sở dữ liệu bị hỏng chỉ mục khóa ngoại giữa bảng Xe Tuần Tra và bảng Vụ Án',
                    'feedback': 'Chỉ mục và cấu trúc bảng hoàn toàn nguyên vẹn; sự cố xuất phát từ thứ tự chiếm dụng tài nguyên.'
                },
                'rc-1': {
                    'text': 'Cả hai dịch vụ đều có lỗi rò rỉ luồng xử lý khiến hệ thống bị hết luồng CPU',
                    'feedback': 'Các luồng xử lý không bị rò rỉ; chúng bị chặn lại (blocked) do đang chờ đợi tài nguyên bị khóa bởi luồng khác.'
                },
                'rc-2': {
                    'text': 'Tắc Nghẽn Phân Tán (Distributed Deadlock do Nghịch Đảo Thứ Tự Khóa) — Dịch vụ Điều Phối khóa Vụ Án rồi chờ khóa Xe Tuần Tra, trong khi Dịch vụ Bảo Trì khóa Xe Tuần Tra rồi chờ khóa Vụ Án',
                    'feedback': 'Chính xác! Đây là hiện tượng Bế Tắc Phân Tán (Deadlock) kinh điển. Dịch vụ A chiếm khóa tài nguyên X và yêu cầu khóa Y; cùng lúc đó Dịch vụ B đã chiếm khóa Y và yêu cầu khóa X. Hai bên giữ chặt tài nguyên của mình và vĩnh viễn chờ đợi đối phương nhượng bộ. Vì khóa được quản lý phân tán qua hai dịch vụ độc lập, cơ sở dữ liệu không thể tự động phát hiện chu trình bế tắc để rollback!'
                },
                'rc-3': {
                    'text': 'Số lượng kết nối đồng thời vượt quá giới hạn max_connections của máy chủ',
                    'feedback': 'Số lượng kết nối vẫn nằm trong ngưỡng cho phép; các tiến trình bị treo cứng vì chờ khóa phân tán.'
                }
            }
        },
        'fix': {
            'question': 'Phương pháp tốt nhất để triệt tiêu vĩnh viễn nguy cơ Bế Tắc Phân Tán (Distributed Deadlock) là gì?',
            'options': {
                'fix-1': {
                    'text': 'Bổ sung thêm thật nhiều luồng xử lý cho cả hai dịch vụ để chúng xử lý nhanh hơn',
                    'feedback': 'Thêm luồng không giải quyết được deadlock — thậm chí còn tạo ra nhiều chu trình bế tắc hơn.'
                },
                'fix-2': {
                    'text': 'Thực thi Thứ Tự Khóa Toàn Cục Nhất Quán (Enforce Global Lock Ordering — tất cả các dịch vụ bắt buộc phải chiếm khóa tài nguyên theo cùng một thứ tự bảng chữ cái hoặc ID cố định), kết hợp Thời Gian Chờ Khóa (Lock Timeout)',
                    'feedback': 'Chính xác! Nguyên lý cốt lõi để loại bỏ Deadlock: "Không có thứ tự khóa nghịch đảo thì không thể có chu trình bế tắc". Nếu quy định rằng: Mọi dịch vụ khi cần cả hai tài nguyên BẮT BUỘC phải chiếm khóa Bảng Vụ Án (Incident) trước rồi mới được chiếm khóa Bảng Xe (Vehicle), thì Dịch vụ Bảo Trì sẽ không bao giờ giữ khóa Xe trước khi có khóa Vụ Án. Kết hợp với Lock Timeout (tự động nhả khóa nếu chờ quá 3s), deadlock sẽ bị triệt tiêu hoàn toàn!'
                },
                'fix-3': {
                    'text': 'Khởi động lại toàn bộ cơ sở dữ liệu mỗi khi phát hiện có giao dịch bị chậm quá 1 phút',
                    'feedback': 'Khởi động lại cơ sở dữ liệu sẽ đánh sập toàn bộ các giao dịch đang diễn ra của toàn thành phố.'
                },
                'fix-4': {
                    'text': 'Chỉ cho phép duy nhất một dịch vụ hoạt động tại một thời điểm',
                    'feedback': 'Chạy tuần tự từng dịch vụ một sẽ phá hủy hoàn toàn khả năng xử lý song song và thông lượng của hệ thống.'
                }
            }
        }
    },
    'case-31': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ dẫn đến việc con số thống kê tổng tội phạm không khớp với danh sách chi tiết các vụ án là gì?',
            'options': {
                'rc-4': {
                    'text': 'Bảng thống kê tội phạm bị lỗi hỏng bộ nhớ RAM trên máy chủ báo cáo',
                    'feedback': 'Phần cứng và bộ nhớ hoàn toàn chính xác; kết quả sai lệch do dữ liệu bị thay đổi giữa hai câu truy vấn.'
                },
                'rc-1': {
                    'text': 'Hàm tính tổng COUNT(*) trong hệ quản trị cơ sở dữ liệu có lỗi tràn số nguyên',
                    'feedback': 'Phép tính COUNT(*) hoạt động hoàn hảo; vấn đề nằm ở mức độ cô lập của giao dịch (Transaction Isolation Level).'
                },
                'rc-2': {
                    'text': 'Hiện Tượng Đọc Bóng Ma (Phantom Read do Mức Cô Lập Read Committed) — trong khi giao dịch báo cáo đang chạy, các đồn cảnh sát khác đã chèn thêm vụ án mới vào cơ sở dữ liệu và được commit',
                    'feedback': 'Chính xác! Báo cáo được tạo bởi hai câu truy vấn trong cùng một phiên: đầu tiên đếm tổng số (COUNT), sau đó lấy danh sách chi tiết (SELECT *). Vì cơ sở dữ liệu hoạt động ở mức cô lập READ COMMITTED, giữa lúc câu lệnh 1 vừa chạy xong và câu lệnh 2 bắt đầu, Đồn 4 đã INSERT và COMMIT 3 vụ án mới. Câu lệnh thứ hai nhìn thấy các bản ghi mới (Phantom Rows) này, khiến tổng danh sách chi tiết là 1.003 vụ trong khi con số tóm tắt ban đầu chỉ ghi nhận 1.000 vụ!'
                },
                'rc-3': {
                    'text': 'Các sĩ quan tại Đồn 4 đã cố tình gian lận số liệu để phá hoại báo cáo của thị trưởng',
                    'feedback': 'Các vụ án được chèn là tội phạm thật xảy ra trong thời gian thực, hoàn toàn hợp lệ.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để đảm bảo tính nhất quán tuyệt đối cho các báo cáo thống kê phức tạp là gì?',
            'options': {
                'fix-1': {
                    'text': 'Nâng mức cô lập lên SERIALIZABLE cho toàn bộ tất cả các truy vấn trên toàn bộ hệ thống',
                    'feedback': 'Serializable là mức cô lập cao nhất nhưng cực kỳ nặng nề, gây xung đột khóa (lock contention) và làm giảm nghiêm trọng thông lượng của các thao tác ghi thông thường.'
                },
                'fix-2': {
                    'text': 'Khóa toàn bộ bảng cơ sở dữ liệu trong suốt thời gian xuất báo cáo của thị trưởng',
                    'feedback': 'Khóa bảng sẽ chặn đứng mọi hoạt động ghi nhận bắt giữ tội phạm của các đồn cảnh sát trong nhiều phút.'
                },
                'fix-3': {
                    'text': 'Sử dụng Mức Cô Lập REPEATABLE READ hoặc SNAPSHOT ISOLATION (dựa trên MVCC) cho giao dịch xuất báo cáo — đảm bảo mọi câu truy vấn trong giao dịch đều đọc từ một ảnh chụp dữ liệu nhất quán tại cùng một thời điểm',
                    'feedback': 'Chính xác! Với REPEATABLE READ hoặc SNAPSHOT ISOLATION (sử dụng cơ chế Đa phiên bản MVCC), khi giao dịch xuất báo cáo bắt đầu, nó sẽ nhận một "ảnh chụp" (snapshot) nhất quán của cơ sở dữ liệu tại thời điểm đó. Bất kỳ thao tác chèn (INSERT) hay sửa đổi nào của các đồn khác diễn ra sau thời điểm bắt đầu giao dịch sẽ hoàn toàn vô hình đối với báo cáo này. Cả câu lệnh COUNT và SELECT chi tiết đều nhìn thấy chính xác cùng 1.000 bản ghi ban đầu!'
                },
                'fix-4': {
                    'text': 'Cấm tất cả các đồn cảnh sát không được ghi nhận tội phạm trong suốt 1 tiếng trước cuộc họp báo',
                    'feedback': 'Không thể tạm dừng công tác bảo vệ trật tự trị an xã hội chỉ để phục vụ cho việc xuất báo cáo.'
                }
            }
        }
    },
    'case-32': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ dẫn đến việc nghi phạm bị giam giữ trong trạng thái lơ lửng không có hồ sơ hợp lệ là gì?',
            'options': {
                'rc-4': {
                    'text': 'Phần mềm của Nhà giam trung tâm bị mất kết nối mạng với phòng trực ban',
                    'feedback': 'Kết nối mạng hoàn toàn bình thường; vấn đề là bước thứ 3 trong quy trình phân tán bị thất bại vì buồng giam đã hết chỗ.'
                },
                'rc-1': {
                    'text': 'Dịch vụ Phân Phòng Giam có lỗi phần mềm báo sai tình trạng hết chỗ trong khi vẫn còn phòng trống',
                    'feedback': 'Buồng giam thực sự đã hết chỗ; sự cố nghiệp vụ này là hoàn toàn bình thường trong vận hành thực tế.'
                },
                'rc-2': {
                    'text': 'Quy Trình Giao Dịch Phân Tán Thiếu Các Hành Động Bù Đắp (Saga Rollback / Compensating Transactions) — khi một bước sau thất bại, các bước trước đã hoàn thành không được hoàn tác, để lại dữ liệu mồ côi không nhất quán',
                    'feedback': 'Chính xác! Quy trình thụ lý nghi phạm là một giao dịch phân tán trải qua 3 vi dịch vụ: (1) Lập hồ sơ bắt giữ, (2) Tạo mã số lưu ký, (3) Phân bổ buồng giam. Khi Bước 3 thất bại do trại giam quá tải, hệ thống không có cơ chế hoàn tác (compensating transactions) cho Bước 1 và Bước 2. Kết quả là nghi phạm có hồ sơ bắt và mã lưu ký nhưng lại không có buồng giam, bị kẹt trong trạng thái lơ lửng không nhất quán!'
                },
                'rc-3': {
                    'text': 'Cả ba dịch vụ lẽ ra phải dùng chung một cơ sở dữ liệu tập trung để thực hiện một giao dịch ACID truyền thống duy nhất',
                    'feedback': 'Dùng chung một cơ sở dữ liệu phá hủy hoàn toàn kiến trúc vi dịch vụ (tính độc lập triển khai, mở rộng và sở hữu dữ liệu). Mô hình Saga là giải pháp tiêu chuẩn cho giao dịch xuyên vi dịch vụ.'
                }
            }
        },
        'fix': {
            'question': 'Phương pháp tốt nhất để xử lý các thất bại trong quy trình giao dịch phân tán đa dịch vụ là gì?',
            'options': {
                'fix-2': {
                    'text': 'Sử dụng giao thức Cam Kết Hai Pha (Two-Phase Commit / 2PC) đồng bộ giữa cả ba dịch vụ',
                    'feedback': '2PC giữ khóa mạng rất lâu, làm giảm thông lượng nghiêm trọng và nếu điều phối viên gặp sự cố, các dịch vụ sẽ bị khóa cứng.'
                },
                'fix-1': {
                    'text': 'Triển khai Mô Hình Saga (Saga Pattern) Với Các Giao Dịch Bù Đắp (Compensating Transactions) — mỗi bước thực thi đều có một hành động "hoàn tác" tương ứng được tự động kích hoạt nếu bước sau gặp thất bại',
                    'feedback': 'Chính xác! Mô hình Saga chia nhỏ giao dịch phân tán thành chuỗi các giao dịch cục bộ độc lập. Mỗi bước đều định nghĩa sẵn hành động bù đắp tương ứng: nếu Bước 3 (phân buồng giam) thất bại, bộ điều phối Saga sẽ tự động kích hoạt "Hành động bù đắp Bước 2" (hủy mã số lưu ký) và tiếp theo là "Hành động bù đắp Bước 1" (hủy hồ sơ bắt giữ). Hệ thống tự động trở về trạng thái sạch sẽ và nhất quán 100%!'
                },
                'fix-3': {
                    'text': 'Thêm logic thử lại liên tục với thời gian chờ số mũ cho đến khi trại giam có buồng trống',
                    'feedback': 'Thử lại vô hạn là điều tối kỵ — buồng giam có thể không có chỗ trong nhiều ngày và nghi phạm sẽ bị kẹt mãi mãi trong trạng thái trung gian.'
                },
                'fix-4': {
                    'text': 'Đặt trước toàn bộ tài nguyên (buồng giam, mã số, hồ sơ) cùng một lúc trước khi thực hiện',
                    'feedback': 'Đặt trước tài nguyên vẫn có thể thất bại khi đặt chỗ và không thể loại trừ hoàn toàn sự cố giữa các bước.'
                }
            }
        }
    },
    'case-33': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ khiến bốn đồn cảnh sát bị mất hoàn toàn khả năng tra cứu lệnh bắt khẩn cấp là gì?',
            'options': {
                'rc-4': {
                    'text': 'Bể luồng xử lý của Cổng Tra Cứu Lệnh Bắt quá nhỏ và cần được tăng kích thước',
                    'feedback': 'Tăng luồng chỉ làm Đồn 3 chiếm dụng nhiều hơn; khi không có giới hạn, tác vụ hàng loạt sẽ nuốt trọn bất kỳ số luồng nào bạn cấp thêm.'
                },
                'rc-1': {
                    'text': 'Tác vụ kiểm tra lệnh bắt hàng loạt của Đồn 3 là một hành vi phá hoại độc hại',
                    'feedback': 'Tác vụ kiểm tra hàng loạt của Đồn 3 là nghiệp vụ hoàn toàn chính đáng để sàng lọc hồ sơ. Vấn đề là nó tiêu thụ tài nguyên vô tội vạ mà không bị kiểm soát.'
                },
                'rc-2': {
                    'text': 'Cơ sở dữ liệu Lệnh bắt Liên bang quá yếu và không thể xử lý khối lượng truy vấn từ các đồn cảnh sát',
                    'feedback': 'Cơ sở dữ liệu hoàn toàn xử lý tốt mức tải 20 truy vấn/giây thông thường. Sự cố xảy ra vì Cổng API bị Đồn 3 dồn dập 500 truy vấn/giây mà không bị điều tiết.'
                },
                'rc-3': {
                    'text': 'Hiện Tượng Người Hàng Xóm Ồn Ào (The Noisy Neighbor Problem) do Cổng Tra Cứu Thiếu Giới Hạn Tốc Độ (No Rate Limiting) — một người dùng duy nhất (Đồn 3) độc chiếm 96% năng lực của API dùng chung, làm bỏ đói toàn bộ các đồn khác',
                    'feedback': 'Chính xác! Khi không có bộ giới hạn tốc độ (Rate Limiting), Cổng API đối xử với tất cả các yêu cầu theo nguyên tắc đến trước phục vụ trước. Đồn 3 kích hoạt một tác vụ quét lô tự động bắn tới 500 yêu cầu/giây, chiếm trọn 96% dung lượng xử lý của toàn bộ hệ thống. Bốn đồn cảnh sát còn lại chỉ còn vài mẩu tài nguyên vụn vặt và liên tục bị timeout khi cần tra cứu khẩn cấp ngoài hiện trường.'
                }
            }
        },
        'fix': {
            'question': 'Phương pháp tốt nhất để ngăn chặn một khách hàng duy nhất làm tê liệt dịch vụ dùng chung là gì?',
            'options': {
                'fix-4': {
                    'text': 'Đặt một hàng đợi FIFO phía trước Cổng Tra Cứu để xử lý các yêu cầu theo đúng thứ tự đến trước phục vụ trước',
                    'feedback': 'Hàng đợi FIFO sẽ bị Đồn 3 bơm đầy 500 yêu cầu/giây, đẩy các yêu cầu tra cứu khẩn cấp của các đồn khác xuống đáy hàng đợi chờ hàng chục phút.'
                },
                'fix-1': {
                    'text': 'Cấm vĩnh viễn và chặn đứng toàn bộ các tác vụ kiểm tra lệnh bắt tự động hàng loạt',
                    'feedback': 'Chặn hoàn toàn các nghiệp vụ hợp lệ là cách tiếp cận tiêu cực. Tác vụ quét lô là cần thiết, chỉ cần điều tiết tốc độ của nó.'
                },
                'fix-2': {
                    'text': 'Triển khai Giới Hạn Tốc Độ Theo Khách Hàng (Per-client Rate Limiting with Quotas dùng Token Bucket hoặc Leaky Bucket), kết hợp Phân Hạng Ưu Tiên (Priority Queues — ưu tiên tra cứu hiện trường thời gian thực hơn tác vụ quét lô)',
                    'feedback': 'Chính xác! Bằng cách cấp hạn mức (quota) công bằng cho từng đồn cảnh sát (ví dụ tối đa 50 req/giây mỗi đồn thông qua thuật toán Token Bucket), Đồn 3 sẽ bị điều tiết nhịp nhàng mà không thể làm nghẽn API. Đồng thời, phân hạng ưu tiên đảm bảo các yêu cầu tra cứu khẩn cấp từ sĩ quan ngoài hiện trường luôn được phục vụ ngay lập tức với độ trễ dưới 100ms, bảo vệ an toàn tối đa cho lực lượng thực thi pháp luật!'
                },
                'fix-3': {
                    'text': 'Mở rộng quy mô máy chủ Cổng Tra Cứu theo chiều ngang vô hạn để đáp ứng bất kỳ mức lưu lượng nào',
                    'feedback': 'Nếu không có giới hạn, Đồn 3 có thể tăng tốc độ quét lên 2.000 req/giây và cơ sở dữ liệu liên bang phía sau cũng có giới hạn trần không thể mở rộng vô tận.'
                }
            }
        }
    }
}
