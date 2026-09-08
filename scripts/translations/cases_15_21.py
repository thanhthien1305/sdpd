# Translations for Cases 15 to 21
DATA = {
    'case-15': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ dẫn đến việc cơ sở dữ liệu bị đánh sập hoàn toàn lúc nửa đêm là gì?',
            'options': {
                'rc-4': {
                    'text': 'Một cuộc tấn công từ chối dịch vụ (DDoS) từ bên ngoài nhắm vào cơ sở dữ liệu lúc nửa đêm',
                    'feedback': 'Lưu lượng đến hoàn toàn từ các dịch vụ nội bộ của sở cảnh sát, không có cuộc tấn công mạng nào từ bên ngoài.'
                },
                'rc-3': {
                    'text': 'Máy chủ Redis bị lỗi phân mảnh bộ nhớ và tự động khởi động lại lúc 00:00',
                    'feedback': 'Redis vẫn chạy liên tục. Vấn đề là hàng chục ngàn khóa trong Redis cùng hết hạn một lúc.'
                },
                'rc-2': {
                    'text': 'Hiện Tượng Tuyết Lở Bộ Đệm (Cache Avalanche) — hàng nghìn khóa cache được cấu hình cùng một thời gian sống TTL cố định, khiến chúng hết hạn đồng loạt tại cùng một giây',
                    'feedback': 'Chính xác! Khi tất cả các khóa được thiết lập cùng một TTL (ví dụ đúng 24 giờ kể từ đợt nạp dữ liệu lúc nửa đêm hôm trước), chúng sẽ đồng loạt bốc hơi khỏi RAM cùng một giây. Toàn bộ các truy vấn đọc sau đó không còn tìm thấy cache, tạo nên một trận tuyết lở yêu cầu dội thẳng xuống cơ sở dữ liệu khiến máy chủ sập nguồn ngay lập tức.'
                },
                'rc-1': {
                    'text': 'Tác vụ sao lưu cơ sở dữ liệu ban đêm đã chiếm dụng toàn bộ tài nguyên I/O đĩa cứng',
                    'feedback': 'Tác vụ sao lưu được lên lịch lúc 03:00 sáng, trong khi sự cố sập cơ sở dữ liệu xảy ra chính xác lúc 00:00:01 do cache hết hạn đồng loạt.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để ngăn chặn hiện tượng Tuyết Lở Bộ Đệm (Cache Avalanche) là gì?',
            'options': {
                'fix-3': {
                    'text': 'Tăng gấp đôi kích thước bộ nhớ RAM của máy chủ Redis để chứa được nhiều khóa hơn',
                    'feedback': 'Dung lượng RAM không phải vấn đề — vấn đề là thời điểm hết hạn của các khóa bị trùng nhau.'
                },
                'fix-1': {
                    'text': 'Áp dụng Độ Lệch Ngẫu Nhiên Vào Thời Gian Sống (TTL Jitter / Staggered Expiration) — thêm một khoảng thời gian ngẫu nhiên vào mỗi khóa khi thiết lập TTL',
                    'feedback': 'Chính xác! Bằng cách thêm một giá trị dao động ngẫu nhiên (jitter), ví dụ TTL = 24 giờ + ngẫu nhiên từ 0 đến 30 phút, các khóa sẽ hết hạn rải rác trong suốt nửa tiếng thay vì tập trung vào đúng một giây. Tải nạp lại dữ liệu xuống DB sẽ được san phẳng mượt mà, triệt tiêu hoàn toàn trận tuyết lở.'
                },
                'fix-2': {
                    'text': 'Tắt hoàn toàn cơ chế hết hạn TTL và để các khóa tồn tại vĩnh viễn trong Redis',
                    'feedback': 'Không có TTL, bộ nhớ Redis sẽ sớm bị cạn kiệt và dữ liệu cũ sẽ không bao giờ được tự động dọn dẹp.'
                },
                'fix-4': {
                    'text': 'Chuyển toàn bộ các truy vấn đọc từ cơ sở dữ liệu sang đọc từ các bản sao lưu trên đĩa',
                    'feedback': 'Bản sao lưu không được thiết kế để phục vụ truy vấn thời gian thực của ứng dụng trực tuyến.'
                }
            }
        }
    },
    'case-16': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ khiến cơ sở dữ liệu bị tê liệt khi bản tin truy nã đặc biệt được công bố là gì?',
            'options': {
                'rc-3': {
                    'text': 'Hệ thống mạng của sở cảnh sát bị nghẽn băng thông do truyền tải hình ảnh độ phân giải cao',
                    'feedback': 'Băng thông mạng vẫn thông suốt. Nút thắt cổ chai nằm ở số lượng kết nối và CPU của cơ sở dữ liệu bị bão hòa.'
                },
                'rc-2': {
                    'text': 'Hiện Tượng Đè Bẹp Bộ Đệm (Dog Pile / Cache Stampede trên Khóa Hot) — khi một thông tin cực kỳ phổ biến bị cache miss lần đầu tiên, hàng nghìn yêu cầu đồng thời cùng chạy xuống DB để nạp dữ liệu cho cùng một bản ghi',
                    'feedback': 'Chính xác! Khi bản tin về nghi phạm nguy hiểm vừa được phát đi, hàng ngàn sĩ quan và hệ thống camera đồng loạt tra cứu mã hồ sơ đó. Vì bản tin mới chưa kịp có trong cache (cold start), tất cả các yêu cầu cùng thấy miss và cùng gửi câu lệnh SELECT xuống cơ sở dữ liệu để tìm cùng một thông tin. Cơ sở dữ liệu bị chôn vùi dưới hàng ngàn truy vấn trùng lặp.'
                },
                'rc-1': {
                    'text': 'Cơ sở dữ liệu bị lỗi khóa bảng (Table Lock) do một quản trị viên đang chạy câu lệnh bảo trì',
                    'feedback': 'Không có câu lệnh quản trị nào chạy lúc đó; tất cả đều là các câu truy vấn SELECT thông thường từ các đồn cảnh sát.'
                },
                'rc-4': {
                    'text': 'Khóa của bản tin trong Redis có kích thước dung lượng quá lớn vượt quá giới hạn mạng',
                    'feedback': 'Kích thước dữ liệu bản ghi rất nhỏ (chưa tới vài KB). Vấn đề là hàng ngàn yêu cầu cùng dồn xuống DB để nạp bản ghi đó.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để bảo vệ cơ sở dữ liệu trước hiện tượng Dog Pile đối với các khóa Hot là gì?',
            'options': {
                'fix-4': {
                    'text': 'Giới hạn số lượng sĩ quan được phép tra cứu thông tin tội phạm truy nã cùng một lúc',
                    'feedback': 'Trong tình huống truy bắt khẩn cấp, ngăn cản sĩ quan tiếp cận thông tin nhận dạng là điều tối kỵ.'
                },
                'fix-1': {
                    'text': 'Nâng cấp cấu hình phần cứng của cơ sở dữ liệu để chịu được 10.000 truy vấn đồng thời',
                    'feedback': 'Nâng cấp phần cứng rất tốn kém và vô nghĩa khi 9.999 truy vấn trong số đó hoàn toàn giống hệt nhau và tính toán ra cùng một kết quả.'
                },
                'fix-2': {
                    'text': 'Sử dụng cơ chế Gộp Yêu Cầu (Singleflight / Request Coalescing) hoặc Khóa Phân Tán (Mutex) — chỉ cho phép đúng 1 tiến trình xuống DB lấy dữ liệu nạp cache, các yêu cầu khác dùng chung kết quả',
                    'feedback': 'Chính xác! Với cơ chế Singleflight (hoặc Mutex Lock tại tầng ứng dụng), khi hàng ngàn yêu cầu đồng thời tìm kiếm cùng một khóa bị miss, hệ thống sẽ gom chúng lại và chỉ ủy quyền cho DUY NHẤT một cuộc gọi xuống cơ sở dữ liệu. Tất cả các yêu cầu còn lại sẽ chờ cuộc gọi đó hoàn thành và cùng nhận kết quả được chia sẻ. Cơ sở dữ liệu chỉ phải xử lý đúng 1 truy vấn!'
                },
                'fix-3': {
                    'text': 'Lưu trữ thông tin tội phạm trong một tệp văn bản tĩnh chia sẻ qua mạng nội bộ',
                    'feedback': 'Tệp văn bản tĩnh không đảm bảo tính toàn vẹn, bảo mật và khó đồng bộ tức thời khi có thông tin mới.'
                }
            }
        }
    },
    'case-17': {
        'rootCause': {
            'question': 'Tại sao mạng CDN vẫn tiếp tục phân phối bức ảnh thẻ căn cước cũ đã 10 năm của kẻ đào tẩu?',
            'options': {
                'rc-1': {
                    'text': 'Nhân viên trực ban đã quên không tải bức ảnh mới lên máy chủ gốc của sở cảnh sát',
                    'feedback': 'Máy chủ gốc đã nhận được bức ảnh mới và đang lưu trữ nó chính xác. Nhật ký cho thấy ảnh mới đã nằm ở máy chủ gốc lúc 08:30.'
                },
                'rc-2': {
                    'text': 'Bộ nhớ đệm của CDN có thời gian sống (TTL) 7 ngày và hệ thống không gửi tín hiệu Xóa Bộ Đệm (Cache Purge) tới CDN khi cập nhật ảnh mới trên máy chủ gốc',
                    'feedback': 'Chính xác! CDN hoạt động theo nguyên tắc lưu bản sao tại các điểm biên mạng (edge nodes) với TTL 7 ngày để giảm tải cho máy chủ gốc. Khi cảnh sát thay đổi ảnh của tội phạm trên máy chủ gốc, CDN ở biên mạng không hề hay biết và vẫn tiếp tục phục vụ bức ảnh cũ được lưu trong bộ nhớ đệm của nó cho công chúng.'
                },
                'rc-3': {
                    'text': 'Trình duyệt web của người dân lưu ảnh cục bộ và từ chối tải lại từ internet',
                    'feedback': 'Ngay cả khi người dùng mở tab ẩn danh hoặc tải từ thiết bị mới tinh, CDN vẫn trả về bức ảnh cũ do máy chủ biên của CDN đang giữ nó.'
                },
                'rc-4': {
                    'text': 'Định dạng tệp ảnh mới không tương thích với mạng phân phối nội dung CDN',
                    'feedback': 'Cả hai ảnh đều là tệp JPEG chuẩn; vấn đề hoàn toàn nằm ở cơ chế lưu đệm của CDN.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để đảm bảo CDN luôn phân phối nội dung mới nhất ngay khi cập nhật là gì?',
            'options': {
                'fix-4': {
                    'text': 'Chờ đợi cho đến khi thời gian sống TTL 7 ngày tự động trôi qua',
                    'feedback': 'Kẻ đào tẩu có thể trốn thoát sang nước khác trong 7 ngày đó; sự an toàn của cộng đồng đòi hỏi hình ảnh phải hiển thị tức thì.'
                },
                'fix-1': {
                    'text': 'Đặt thời gian sống TTL của CDN về mức 0 giây cho tất cả các bức ảnh',
                    'feedback': 'Đặt TTL = 0 làm mất hoàn toàn tác dụng của CDN, biến CDN thành một proxy thông thường và đẩy toàn bộ tải về máy chủ gốc.'
                },
                'fix-2': {
                    'text': 'Tích hợp lệnh Xóa Bộ Đệm CDN (CDN Cache Purge / Invalidation API) vào quy trình cập nhật nội dung, hoặc sử dụng Đặt Tên Tệp Theo Băm Phiên Bản (URL Versioning / Cache Busting)',
                    'feedback': 'Chính xác! Hai giải pháp tiêu chuẩn công nghiệp: (1) Gọi API Purge của CDN ngay khi cập nhật ảnh để ép các máy chủ biên xóa bản sao cũ ngay lập tức; hoặc (2) Sử dụng URL có gắn mã băm phiên bản (ví dụ suspect_v2.jpg hoặc ?v=hash). Khi ảnh đổi, URL đổi theo, CDN sẽ coi đó là tài nguyên mới và nạp ngay bức ảnh mới nhất mà không sợ dữ liệu cũ.'
                },
                'fix-3': {
                    'text': 'Tắt hoàn toàn mạng CDN và để toàn bộ người dân truy cập thẳng vào máy chủ gốc của sở cảnh sát',
                    'feedback': 'Khi hàng triệu người dân cùng truy cập xem ảnh truy nã, máy chủ gốc của sở cảnh sát sẽ sập ngay lập tức vì quá tải băng thông.'
                }
            }
        }
    },
    'case-18': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ khiến 23 tin nhắn điều động khẩn cấp bị mất tích hoàn toàn là gì?',
            'options': {
                'rc-4': {
                    'text': 'Xe tuần tra bị mất sóng bộ đàm trong khi đang di chuyển qua khu vực đường hầm',
                    'feedback': 'Xe tuần tra vẫn nhận các lệnh điều động khác bình thường. Sự cố xảy ra tại máy chủ môi giới tin nhắn (broker).'
                },
                'rc-3': {
                    'text': 'Các sĩ quan trực ban đã xóa nhầm 23 tin nhắn khỏi hệ thống điều phối trung tâm',
                    'feedback': 'Nhật ký cho thấy các tin nhắn đã được hệ thống tiếp nhận và gửi vào hàng đợi thành công lúc 19:42.'
                },
                'rc-2': {
                    'text': 'Hàng đợi tin nhắn hoạt động ở chế độ Chỉ Lưu Trong Bộ Nhớ RAM (In-Memory Only) mà không có Tính Bền Vững (Persistence) ra đĩa cứng — khi máy chủ hàng đợi sập, toàn bộ tin nhắn chưa xử lý bốc hơi',
                    'feedback': 'Chính xác! Máy chủ hàng đợi tin nhắn (Message Queue) được cấu hình chế độ tạm thời (transient / in-memory) để tối đa hóa tốc độ. Khi tiến trình hàng đợi bị sập hoặc khởi động lại, 23 lệnh điều phối khẩn cấp đang nằm chờ trong bộ nhớ RAM đã biến mất hoàn toàn mà không để lại dấu vết.'
                },
                'rc-1': {
                    'text': 'Các tin nhắn gửi đến có định dạng JSON không hợp lệ và bị bộ phân tích cú pháp từ chối',
                    'feedback': 'Tất cả các tin nhắn đều hợp lệ và đã được hàng đợi chấp nhận vào RAM trước khi tiến trình bị sập.'
                }
            }
        },
        'fix': {
            'question': 'Hạ tầng hàng đợi tin nhắn cần được cấu hình như thế nào để đảm bảo không bao giờ mất thông điệp?',
            'options': {
                'fix-3': {
                    'text': 'Tăng dung lượng RAM máy chủ lên gấp 4 lần để hàng đợi không bao giờ bị sập do thiếu bộ nhớ',
                    'feedback': 'Tăng RAM không giải quyết được các sự cố mất điện, cập nhật hệ điều hành hoặc lỗi sập tiến trình phần mềm.'
                },
                'fix-1': {
                    'text': 'Cấu hình Hàng Đợi Bền Vững (Durable Queues) và Thông Điệp Bền Vững (Persistent Messages ghi xuống đĩa cứng), kết hợp Xác Nhận Tin Nhắn Từ Phía Người Dùng (Consumer Acknowledgements / ACK)',
                    'feedback': 'Chính xác! Bằng cách kích hoạt chế độ lưu trữ bền vững (Write-Ahead Log / fsync ra đĩa cứng) trên hàng đợi và bắt buộc Consumer chỉ gửi ACK sau khi đã hoàn thành xử lý nhiệm vụ, nếu máy chủ hàng đợi bị sập và khởi động lại, nó sẽ đọc lại toàn bộ thông điệp từ đĩa cứng và phân phối lại cho các xe tuần tra. Không một tin nhắn nào bị bỏ sót.'
                },
                'fix-2': {
                    'text': 'Yêu cầu tổng đài viên gọi điện thoại trực tiếp cho từng xe tuần tra thay vì dùng phần mềm',
                    'feedback': 'Gọi điện thoại thủ công cho hàng trăm xe tuần tra trong giờ cao điểm là điều bất khả thi và làm chậm trễ nghiêm trọng việc cứu nạn.'
                },
                'fix-4': {
                    'text': 'Chuyển sang giao thức UDP để truyền tin nhắn nhanh hơn tới các xe tuần tra',
                    'feedback': 'UDP là giao thức không đảm bảo phân phối tin cậy và chấp nhận rớt gói tin — điều này sẽ càng làm mất tin nhắn nhiều hơn.'
                }
            }
        }
    },
    'case-19': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ dẫn đến việc hai đội cảnh sát cùng ập tới bắt giữ một nghi phạm hai lần là gì?',
            'options': {
                'rc-4': {
                    'text': 'Thẩm phán đã vô tình ký hai lệnh bắt giữ giống hệt nhau cho cùng một nghi phạm',
                    'feedback': 'Chỉ có duy nhất một lệnh bắt giữ được ban hành và đưa vào hệ thống.'
                },
                'rc-1': {
                    'text': 'Hàng đợi tin nhắn bị lỗi phần mềm khiến nó tự động nhân bản thông điệp thành hai bản sao',
                    'feedback': 'Hàng đợi hoạt động theo đúng ngữ nghĩa "Phân phối ít nhất một lần" (At-least-once delivery). Khi Consumer 1 xử lý quá lâu và hết hạn thời gian chờ xác nhận (ACK timeout), hàng đợi buộc phải phát lại tin nhắn đó cho Consumer 2.'
                },
                'rc-3': {
                    'text': 'Hai đồn cảnh sát cạnh tranh thành tích phá án và cố tình tranh nhau lệnh bắt',
                    'feedback': 'Cả hai đội đều hành động hoàn toàn độc lập dựa trên chỉ thị chính thức từ phần mềm điều động.'
                },
                'rc-2': {
                    'text': 'Dịch vụ xử lý lệnh bắt Thiếu Tính Lũy Thừa (Non-Idempotent Consumer) trong mô hình Phân Phối Ít Nhất Một Lần (At-Least-Once Delivery) — tin nhắn được gửi lại nhưng hệ thống không kiểm tra xem lệnh đã được xử lý chưa',
                    'feedback': 'Chính xác! Trong mạng phân tán, cơ chế At-least-once delivery luôn có thể gửi lại thông điệp (do mạng chập chờn hoặc timeout xử lý). Consumer xử lý lệnh bắt đã không kiểm tra tính lũy thừa (Idempotency) mà mù quáng điều động xe cho mỗi lần nhận được thông điệp. Kết quả là cả hai đội tuần tra đều được phái đi bắt cùng một người.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để ngăn ngừa việc xử lý trùng lặp thông điệp trong hệ thống hàng đợi là gì?',
            'options': {
                'fix-4': {
                    'text': 'Bổ sung tầng lọc trùng lặp bên trong máy chủ hàng đợi để tự động loại bỏ các tin nhắn trùng lặp',
                    'feedback': 'Khử trùng tại hàng đợi chỉ lọc được các thông điệp giống hệt nhau trên đường truyền, không bảo vệ được logic nghiệp vụ ở tầng ứng dụng khi có sự cố xử lý dở dang.'
                },
                'fix-1': {
                    'text': 'Nâng cấp toàn bộ hạ tầng hàng đợi sang hỗ trợ ngữ nghĩa Phân Phối Đúng Một Lần (Exactly-Once Delivery)',
                    'feedback': 'Exactly-once thuần túy qua mạng phân tán là điều cực kỳ tốn kém và bất khả thi nếu các hệ thống phụ trợ không hỗ trợ giao dịch 2 pha phân tán.'
                },
                'fix-2': {
                    'text': 'Xây dựng Consumer có Tính Lũy Thừa (Idempotent Consumer) — theo dõi mã định danh thông điệp / mã lệnh bắt (Idempotency Key) và bỏ qua nếu đã được xử lý',
                    'feedback': 'Chính xác! Một Consumer lũy thừa sẽ lưu trạng thái các mã lệnh bắt đã xử lý vào bảng cơ sở dữ liệu có ràng buộc UNIQUE. Khi nhận được một thông điệp (dù là lần đầu hay lần thứ 10), nó kiểm tra xem mã lệnh đó đã được xử lý chưa. Nếu đã xử lý, nó lập tức bỏ qua và gửi xác nhận ACK. Dù tin nhắn có bị gửi lại bao nhiêu lần, hành động thực tế cũng chỉ diễn ra đúng một lần duy nhất!'
                },
                'fix-3': {
                    'text': 'Tăng thời gian chờ ACK timeout của hàng đợi từ 30 giây lên 5 phút',
                    'feedback': 'Tăng timeout chỉ làm giảm xác suất gửi lại, nhưng nếu Consumer thực sự bị sập, tin nhắn sẽ bị giam giữ tới 5 phút mới được gửi lại cho máy khác.'
                }
            }
        }
    },
    'case-20': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ khiến đường ống điều động bị ùn ứ hàng chục nghìn thông điệp là gì?',
            'options': {
                'rc-1': {
                    'text': 'Tổng đài 911 tạo ra lượng tin nhắn điều phối quá nhanh vượt quá khả năng tiếp nhận của hàng đợi',
                    'feedback': 'Tốc độ sản xuất 12 tin/giây là hoàn toàn bình thường. Vấn đề là đầu tiêu thụ (consumer) bằng 0 vì dịch vụ đã bị sập.'
                },
                'rc-2': {
                    'text': 'Sự Cố Thiếu Cơ Chế Áp Lực Ngược (Backpressure Failure) khi dịch vụ Consumer bị sập mà không có chính sách tự khởi động lại — tin nhắn tiếp tục đổ về vô hạn mà không có ai tiêu thụ',
                    'feedback': 'Chính xác! Dịch vụ Consumer điều phối đã bị sập do tràn bộ nhớ từ 45 phút trước và không có cơ chế giám sát tự động hồi sinh. Tổng đài vẫn liên tục đẩy tin nhắn vào hàng đợi trong khi không có ai rút tin ra. Hệ thống thiếu cơ chế áp lực ngược (backpressure) để giới hạn độ sâu hàng đợi hoặc điều tiết đầu vào, khiến hàng đợi phình to tới 91% RAM và sắp sập toàn diện.'
                },
                'rc-3': {
                    'text': 'Máy chủ hàng đợi tin nhắn bị hết bộ nhớ RAM và từ chối nhận các tin nhắn mới',
                    'feedback': 'Hàng đợi đang ở mức 91% RAM và vẫn đang gắng gượng nhận tin. Hết bộ nhớ là triệu chứng của vấn đề thiếu áp lực ngược chứ không phải nguyên nhân gốc.'
                },
                'rc-4': {
                    'text': 'Phân vùng mạng đã chia cắt máy chủ hàng đợi với các xe tuần tra',
                    'feedback': 'Xe tuần tra không kết nối trực tiếp vào hàng đợi; dịch vụ consumer trung gian mới là bên kết nối. Consumer đã chết do lỗi OutOfMemoryError.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để ngăn chặn tình trạng đường ống tin nhắn bị tắc nghẽn vô hạn trong tương lai là gì?',
            'options': {
                'fix-3': {
                    'text': 'Để tổng đài 911 gửi lệnh trực tiếp tới xe tuần tra mà không cần đi qua hàng đợi trung gian',
                    'feedback': 'Bỏ hàng đợi làm mất đi lớp đệm hấp thụ các đợt tăng vọt lưu lượng trong giờ cao điểm.'
                },
                'fix-2': {
                    'text': 'Nâng cấp dung lượng RAM của máy chủ hàng đợi lên 64 GB để chứa được nhiều tin nhắn hơn',
                    'feedback': 'Nâng RAM chỉ trì hoãn cái chết — nếu Consumer vẫn bị chết, hàng đợi sẽ lấp đầy bất kỳ dung lượng RAM nào bạn cấp cho nó.'
                },
                'fix-1': {
                    'text': 'Triển khai Kiểm Soát Áp Lực Ngược (Backpressure Controls): tự động giám sát và hồi sinh Consumer, giới hạn dung lượng tối đa của hàng đợi, và điều tiết tốc độ Producer khi hàng đợi bị đầy',
                    'feedback': 'Chính xác! Một hệ thống đường ống hoàn chỉnh bắt buộc phải có: (1) Trình giám sát tiến trình tự động khởi động lại Consumer khi bị lỗi, (2) Thiết lập kích thước hàng đợi tối đa, và (3) Cơ chế Áp lực ngược (Backpressure) phát tín hiệu cho bên gửi giảm tốc độ hoặc từ chối bớt yêu cầu khi người tiêu thụ không theo kịp. Điều này giúp bảo vệ hệ thống không bị tràn bộ nhớ.'
                },
                'fix-4': {
                    'text': 'Cấu hình các tin nhắn điều động tự động hết hạn và tự xóa sau 5 phút nếu chưa được tiêu thụ',
                    'feedback': 'Tự động xóa tin nhắn điều phối đồng nghĩa với việc các cuộc gọi khẩn cấp của người dân bị vứt bỏ vào hư vô.'
                }
            }
        }
    },
    'case-21': {
        'rootCause': {
            'question': 'Tại sao các báo cáo phá án của cùng một vụ việc lại đến cơ quan công tố theo thứ tự thời gian lộn xộn?',
            'options': {
                'rc-4': {
                    'text': 'Hàng đợi tin nhắn có lỗi phần mềm khiến nó phân phối thông điệp ra khỏi thứ tự FIFO',
                    'feedback': 'Hàng đợi vẫn đẩy tin theo thứ tự FIFO tới từng Consumer. Vấn đề là có nhiều Consumer xử lý song song với tốc độ khác nhau.'
                },
                'rc-1': {
                    'text': 'API tiếp nhận báo cáo đã nạp các bản ghi vào hàng đợi sai thứ tự thời gian',
                    'feedback': 'Nhật ký API cho thấy các báo cáo được đẩy vào hàng đợi hoàn toàn chuẩn xác theo trình tự thời gian xảy ra.'
                },
                'rc-2': {
                    'text': 'Nhiều Consumer xử lý song song với tốc độ không đồng đều — Consumer xử lý thông điệp sau xong nhanh hơn Consumer đang xử lý thông điệp trước, phá vỡ thứ tự ban đầu',
                    'feedback': 'Chính xác! Hàng đợi sử dụng cơ chế Round-Robin để chia đều các thông điệp cho 3 Consumer chạy song song mà không có khóa phân vùng. Thông điệp "Bắt giữ" (bước 1) rơi vào Consumer chậm, trong khi thông điệp "Khởi tố" (bước 2) rơi vào Consumer nhanh. Consumer nhanh hoàn thành và ghi vào cơ sở dữ liệu trước, khiến viện công tố thấy nghi phạm bị khởi tố trước khi bị bắt giữ!'
                },
                'rc-3': {
                    'text': 'Cơ sở dữ liệu của Viện công tố tự ý sắp xếp lại bản ghi theo thứ tự ngẫu nhiên',
                    'feedback': 'Cơ sở dữ liệu chỉ ghi nhận và hiển thị theo đúng thứ tự mà các Consumer ghi dữ liệu vào.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để đảm bảo thứ tự thời gian của các báo cáo thuộc cùng một vụ án là gì?',
            'options': {
                'fix-2': {
                    'text': 'Sử dụng Khóa Phân Vùng (Partition Keys theo Case ID) — đảm bảo tất cả thông điệp của cùng một vụ án luôn được định tuyến tới cùng một Consumer để xử lý tuần tự',
                    'feedback': 'Chính xác! Bằng cách gán Partition Key là Case ID (như trong Kafka hoặc AWS Kinesis), tất cả các sự kiện thuộc cùng Vụ án 77 chắc chắn sẽ vào cùng một phân vùng (partition) và được tiêu thụ tuần tự bởi duy nhất một Consumer theo đúng thứ tự FIFO. Trong khi đó, các vụ án khác vẫn được xử lý song song trên các phân vùng khác. Hệ thống vừa bảo toàn thứ tự, vừa giữ được thông lượng cao!'
                },
                'fix-1': {
                    'text': 'Giảm số lượng Consumer xuống đúng 1 Consumer duy nhất để xử lý tuần tự từng thông điệp một',
                    'feedback': 'Dùng 1 Consumer giải quyết được thứ tự nhưng triệt tiêu hoàn toàn khả năng xử lý song song, biến Consumer thành nút thắt cổ chai cho toàn thành phố.'
                },
                'fix-3': {
                    'text': 'Đính kèm nhãn thời gian vào báo cáo và chạy câu lệnh sắp xếp lại trong cơ sở dữ liệu sau khi chèn',
                    'feedback': 'Sắp xếp hậu kỳ rất mong manh vì bạn không thể biết khi nào toàn bộ các thông điệp của một vụ án đã đến đủ để tiến hành sắp xếp.'
                },
                'fix-4': {
                    'text': 'Chuẩn hóa phần cứng của tất cả các máy chủ Consumer để chúng chạy với tốc độ giống hệt nhau từng mili-giây',
                    'feedback': 'Thời gian xử lý phụ thuộc vào độ phức tạp của dữ liệu, độ trễ mạng và dừng dọn rác (GC pause). Không phần cứng nào đảm bảo tốc độ giống nhau 100%.'
                }
            }
        }
    }
}
