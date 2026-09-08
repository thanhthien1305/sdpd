# Translations for Cases 01 to 07
# Format: { 'case-NN': { 'rootCause': { 'question': ..., 'options': { 'id': { 'text': ..., 'feedback': ... } } }, 'fix': ... } }

DATA = {
    'case-01': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ gây ra sự cố mất điện toàn hệ thống là gì?',
            'options': {
                'rc-4': {
                    'text': 'Quá nhiều truy vấn đồng thời từ tất cả các đồn cảnh sát cùng lúc đã làm quá tải máy chủ cơ sở dữ liệu',
                    'feedback': 'Nhật ký cho thấy lưu lượng truy cập ở mức bình thường (khoảng 120 truy vấn/giây) cho đến khi máy chủ gặp sự cố phần cứng. Đây không phải là sự cố do quá tải lưu lượng.'
                },
                'rc-2': {
                    'text': 'Máy chủ cơ sở dữ liệu duy nhất là một Điểm Lỗi Đơn (SPOF) — khi phần cứng của nó gặp sự cố, toàn bộ hệ thống sụp đổ vì không có bản sao dự phòng',
                    'feedback': 'Chính xác! Hệ thống phụ thuộc hoàn toàn vào một máy chủ cơ sở dữ liệu duy nhất. Khi nguồn điện hoặc bo mạch chủ của máy chủ đó bị hỏng, toàn bộ sở cảnh sát không còn nơi nào để truy vấn hay lưu trữ dữ liệu. Một hệ thống phân tán đáng tin cậy luôn phải có các bản sao (replicas) dự phòng.'
                },
                'rc-1': {
                    'text': 'Một sự cố phân vùng mạng đang ngăn cản các đồn cảnh sát kết nối tới trung tâm dữ liệu',
                    'feedback': 'Hạ tầng mạng hoàn toàn bình thường. Sự cố xảy ra trực tiếp tại máy chủ cơ sở dữ liệu do hỏng phần cứng, không phải lỗi đường truyền mạng.'
                },
                'rc-3': {
                    'text': 'Cơ sở dữ liệu đã vượt quá dung lượng lưu trữ tối đa và tự động dừng xử lý để bảo vệ dữ liệu',
                    'feedback': 'Dung lượng ổ đĩa vẫn còn trống hơn 40%. Nguyên nhân là do hỏng hóc phần cứng đột ngột, không phải do cạn kiệt dung lượng đĩa.'
                }
            }
        },
        'fix': {
            'question': 'Giải pháp tốt nhất để ngăn chặn sự cố này tái diễn trong tương lai là gì?',
            'options': {
                'fix-4': {
                    'text': 'Lắp đặt phần cứng tốt hơn với mảng đĩa RAID dự phòng trên chính máy chủ cơ sở dữ liệu hiện tại',
                    'feedback': 'Mảng đĩa RAID chỉ bảo vệ khi một ổ cứng bị lỗi vật lý. Nó không thể cứu hệ thống nếu nguồn điện, bo mạch chủ, hệ điều hành hoặc toàn bộ trung tâm dữ liệu gặp sự cố. Bạn cần dự phòng ở cấp độ toàn bộ máy chủ.'
                },
                'fix-3': {
                    'text': 'Cung cấp cho mỗi đồn cảnh sát một bản sao cơ sở dữ liệu độc lập riêng biệt để họ tự quản lý',
                    'feedback': 'Cách tiếp cận này dẫn đến việc phân mảnh dữ liệu nghiêm trọng — các đồn sẽ không nhìn thấy dữ liệu tội phạm của nhau và xung đột dữ liệu sẽ xảy ra liên tục.'
                },
                'fix-1': {
                    'text': 'Triển khai cơ chế sao chép cơ sở dữ liệu (Replication) — duy trì ít nhất một bản sao (replica) có khả năng tự động thăng cấp thành Leader khi nút chính gặp lỗi',
                    'feedback': 'Chính xác! Bằng cách thiết lập mô hình Leader-Follower với khả năng chuyển đổi dự phòng (failover), nếu máy chủ Leader gặp sự cố phần cứng, hệ thống sẽ tự động thăng cấp bản sao Follower lên làm Leader mới trong vài giây, loại bỏ hoàn toàn điểm lỗi đơn lẻ (SPOF).'
                },
                'fix-2': {
                    'text': 'Tăng tần suất sao lưu dữ liệu từ 72 giờ lên tự động sao lưu mỗi giờ một lần',
                    'feedback': 'Sao lưu thường xuyên hơn giúp khôi phục dữ liệu đã lưu tốt hơn, nhưng nó không giúp hệ thống duy trì tính sẵn sàng (High Availability). Hệ thống vẫn sẽ bị ngừng hoạt động nhiều giờ trong khi chờ dựng lại máy chủ từ bản backup.'
                }
            }
        }
    },
    'case-02': {
        'rootCause': {
            'question': 'Tại sao Sĩ quan Chen lại nhìn thấy lệnh bắt giữ vẫn còn hiệu lực trong khi thẩm phán đã hủy bỏ nó?',
            'options': {
                'rc-3': {
                    'text': 'Sự cố phân vùng mạng đã ngăn Đồn Nam nhận các bản ghi cập nhật từ máy chủ cơ sở dữ liệu Leader',
                    'feedback': 'Máy chủ bản sao Đồn Nam vẫn kết nối mạng bình thường và vẫn nhận các sự kiện nhân bản. Vấn đề là tiến trình xử lý hàng đợi nhân bản bị tụt lại quá xa so với máy chủ chính.'
                },
                'rc-4': {
                    'text': 'Máy chủ cơ sở dữ liệu Leader có lỗi phần mềm khiến nó không gửi các bản ghi cập nhật lệnh bắt tới Follower Đồn Nam',
                    'feedback': 'Nhật ký của Leader ghi nhận rõ sự kiện nhân bản đã được phát đi thành công, nhưng phía Follower đang bị tồn đọng một lượng lớn tác vụ đọc làm chậm tiến trình áp dụng dữ liệu.'
                },
                'rc-2': {
                    'text': 'Thiết bị của Sĩ quan Chen được định tuyến tới một máy chủ Follower có độ trễ nhân bản (Replication Lag) quá lớn, dẫn đến việc phục vụ dữ liệu đã lỗi thời (Stale Read)',
                    'feedback': 'Chính xác! Trong mô hình nhân bản bất đồng bộ, các bản sao Follower luôn có độ trễ nhất định so với Leader. Đồn Nam bị trễ tới hơn 4 tiếng do nghẽn I/O. Khi Sĩ quan Chen tra cứu, yêu cầu được gửi tới Follower chưa cập nhật lệnh hủy bỏ của thẩm phán, dẫn đến việc bắt giữ oan người vô tội.'
                },
                'rc-1': {
                    'text': 'Lệnh hủy bỏ của thẩm phán chưa bao giờ được lưu do giao dịch ghi vào máy chủ Leader thất bại âm thầm',
                    'feedback': 'Nhật ký của Leader xác nhận giao dịch ghi lệnh hủy bỏ đã COMMIT thành công lúc 14:15. Vấn đề nằm ở việc dữ liệu đó chưa kịp truyền tải tới máy chủ Follower.'
                }
            }
        },
        'fix': {
            'question': 'Phương pháp tốt nhất để ngăn chặn các sĩ quan hành động dựa trên dữ liệu lệnh bắt lỗi thời là gì?',
            'options': {
                'fix-4': {
                    'text': 'Lưu tạm trạng thái lệnh bắt giữ cục bộ trên từng thiết bị của sĩ quan để tăng tốc độ truy vấn',
                    'feedback': 'Lưu cache cục bộ trên máy sĩ quan chỉ làm vấn đề dữ liệu cũ trở nên tồi tệ hơn gấp bội! Sĩ quan sẽ nhìn thấy dữ liệu cũ kỹ hơn nữa.'
                },
                'fix-1': {
                    'text': 'Định tuyến các truy vấn nhạy cảm và quan trọng (như kiểm tra lệnh bắt giữ) trực tiếp về máy chủ Leader thay vì đọc từ Followers',
                    'feedback': 'Chính xác! Đối với các dữ liệu có rủi ro pháp lý hoặc an toàn tính mạng cao, bạn không thể chấp nhận tính nhất quán cuối cùng (eventual consistency). Việc đọc trực tiếp từ Leader (Read-from-Leader) hoặc bắt buộc kiểm tra giới hạn độ trễ (bounded staleness) đảm bảo sĩ quan luôn nhìn thấy dữ liệu mới nhất được xác nhận.'
                },
                'fix-3': {
                    'text': 'Bổ sung thêm nhiều máy chủ bản sao Follower tại các đồn cảnh sát để phân tán tải truy vấn đọc',
                    'feedback': 'Thêm nhiều Follower không giải quyết được độ trễ nhân bản của Follower hiện tại — thậm chí nó có thể khiến Leader tốn thêm tài nguyên mạng để nhân bản tới nhiều nơi hơn.'
                },
                'fix-2': {
                    'text': 'Chuyển toàn bộ các Follower từ chế độ nhân bản bất đồng bộ sang nhân bản đồng bộ hoàn toàn',
                    'feedback': 'Nhân bản đồng bộ tới TOÀN BỘ các bản sao sẽ khiến một bản sao chậm làm nghẽn toàn bộ hoạt động ghi của cả thành phố. Nếu Đồn Nam bị chậm mạng, không thẩm phán nào có thể ban hành hay hủy lệnh bắt mới.'
                }
            }
        }
    },
    'case-03': {
        'rootCause': {
            'question': 'Tại sao 16 trong tổng số 47 bức ảnh hiện trường lại bị mất vĩnh viễn?',
            'options': {
                'rc-3': {
                    'text': 'Cơ chế nhân bản bất đồng bộ cho phép Leader báo thành công cho client trước khi dữ liệu được nhân bản sang Replica — khi Leader bị sập nguồn, dữ liệu chưa truyền đi bị mất vĩnh viễn',
                    'feedback': 'Chính xác! Với nhân bản bất đồng bộ, Leader xác nhận đã ghi nhận ảnh ngay khi nó lưu vào đĩa cục bộ mà không cần chờ Follower xác nhận. Khi Leader bị sập nguồn đột ngột, các ảnh từ 32 đến 47 mới chỉ nằm trên Leader cũ và chưa truyền sang Follower. Khi Follower được thăng cấp lên làm Leader mới, nó hoàn toàn không có 16 bức ảnh này.'
                },
                'rc-1': {
                    'text': 'Quá trình tải lên của đội pháp y bị gián đoạn giữa chừng và không phải toàn bộ 47 bức ảnh đều được gửi trọn vẹn lên máy chủ',
                    'feedback': 'Nhật ký tải lên cho thấy rõ ràng toàn bộ 47 ảnh đã được máy chủ tiếp nhận thành công và trả về mã HTTP 200 OK lúc 22:03. Dữ liệu bị mất sau khi tải lên, trong quá trình nhân bản giữa các máy chủ.'
                },
                'rc-4': {
                    'text': 'Sự cố phân vùng mạng đã cắt đứt kết nối giữa Leader và Follower, ngăn chặn toàn bộ lưu lượng nhân bản',
                    'feedback': 'Nhật ký cho thấy các ảnh 1-31 đã được nhân bản trơn tru ngay trước khi Leader sập. Không hề có phân vùng mạng — Leader bị chết phần cứng trước khi kịp nhân bản nốt các ảnh còn lại.'
                },
                'rc-2': {
                    'text': 'Cơ sở dữ liệu Follower bị hết dung lượng lưu trữ được cấp phát và bắt đầu từ chối dữ liệu ảnh gửi tới',
                    'feedback': 'Follower đã lưu trữ thành công 31 bức ảnh đầu tiên và dung lượng đĩa vẫn còn rất nhiều. 16 ảnh còn lại chưa từng được Leader gửi sang.'
                }
            }
        },
        'fix': {
            'question': 'Hệ thống lưu trữ chứng cứ cần được thay đổi như thế nào để ngăn mất mát dữ liệu khi chuyển đổi dự phòng (failover)?',
            'options': {
                'fix-2': {
                    'text': 'Thêm một bản sao Follower thứ hai để tăng số lượng máy chủ nhận bản sao và tăng xác suất dữ liệu sống sót',
                    'feedback': 'Nếu tất cả Follower đều dùng cơ chế bất đồng bộ, việc có thêm Follower thứ hai không loại bỏ được khoảng hở mất dữ liệu. Leader vẫn báo thành công trước khi bất kỳ Follower nào nhận được dữ liệu.'
                },
                'fix-3': {
                    'text': 'Tăng tốc độ băng thông nhân bản để dữ liệu được gửi sang Follower nhanh hơn, thu hẹp khoảng thời gian chưa nhân bản',
                    'feedback': 'Tăng tốc độ truyền tải giúp thu hẹp khoảng hở thời gian rủi ro nhưng KHÔNG THỂ loại bỏ nó hoàn toàn. Khi lưu lượng ghi tăng vọt hoặc sập nguồn bất ngờ, nguy cơ mất dữ liệu vẫn luôn tồn tại. Chỉ có nhân bản đồng bộ mới cam kết không mất dữ liệu.'
                },
                'fix-4': {
                    'text': 'Tắt hoàn toàn cơ chế chuyển đổi dự phòng tự động — giữ hệ thống ngoại tuyến và chờ Leader cũ khởi động lại',
                    'feedback': 'Giải pháp này có thể cứu được dữ liệu (nếu đĩa cứng không hỏng), nhưng cái giá phải trả là hệ thống ngừng hoạt động trong nhiều giờ. Hệ thống bằng chứng tư pháp cần cả tính sẵn sàng cao LẪN tính bền vững dữ liệu.'
                },
                'fix-1': {
                    'text': 'Sử dụng cơ chế nhân bản đồng bộ (Synchronous Replication) hoặc bán đồng bộ cho dữ liệu quan trọng — Leader phải chờ ít nhất một bản sao xác nhận đã ghi trước khi báo thành công cho client',
                    'feedback': 'Chính xác! Với nhân bản đồng bộ, Leader không bao giờ gửi phản hồi xác nhận cho client cho đến khi ít nhất một bản sao Follower đã nhận và ghi dữ liệu an toàn. Nếu Leader sập, bản sao được thăng cấp chắc chắn nắm giữ đầy đủ 100% dữ liệu đã xác nhận. Mặc dù độ trễ ghi tăng nhẹ, đây là sự đánh đổi bắt buộc cho sự toàn vẹn của bằng chứng pháp y.'
                }
            }
        }
    },
    'case-04': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ dẫn đến việc hồ sơ nghi phạm bị xung đột dữ liệu trái ngược nhau là gì?',
            'options': {
                'rc-4': {
                    'text': 'Thời gian chờ (timeout) chuyển đổi dự phòng tự động được cấu hình quá thấp, gây ra việc thăng cấp sớm',
                    'feedback': 'Thời gian timeout ngắn có thể làm thăng cấp nhanh, nhưng nguyên nhân sâu xa là cả hai phía đều không hề biết đến sự tồn tại của phía bên kia do mạng bị đứt, và không bên nào kiểm tra túc số đa số (quorum).'
                },
                'rc-3': {
                    'text': 'Một sĩ quan tại Đồn Đông đã thực hiện cập nhật trái phép vào hồ sơ nghi phạm mà không có quyền hạn',
                    'feedback': 'Cả hai sĩ quan đều là người dùng hợp lệ và có thẩm quyền. Hệ thống đã chấp nhận cả hai thao tác ghi một cách độc lập trên hai máy chủ cơ sở dữ liệu khác nhau.'
                },
                'rc-1': {
                    'text': 'Lỗi phần mềm bên trong một trong các nút cơ sở dữ liệu làm hỏng dữ liệu trạng thái của nghi phạm',
                    'feedback': 'Cả hai máy chủ đều hoạt động hoàn hảo theo logic của chúng. Không có lỗi hỏng bộ nhớ hay hỏng phần mềm; vấn đề nằm ở kiến trúc điều phối mạng phân tán.'
                },
                'rc-2': {
                    'text': 'Sự cố phân vùng mạng gây ra hiện tượng Phân Não (Split-Brain) — cả hai trung tâm dữ liệu đều tự thăng cấp máy chủ của mình làm Leader và chấp nhận các lệnh ghi mâu thuẫn',
                    'feedback': 'Chính xác! Sự cố đứt cáp quang giữa Đồn Tây và Đồn Đông đã chia đôi hệ thống mạng. Vì thiếu cơ chế đồng thuận kiểm tra túc số (quorum), Đồn Đông tưởng Đồn Tây đã chết nên tự thăng cấp bản sao của mình lên làm Leader, trong khi Đồn Tây vẫn đang là Leader. Cả hai Leader đều độc lập chấp nhận các lệnh ghi trái ngược nhau cho cùng một nghi phạm!'
                }
            }
        },
        'fix': {
            'question': 'Phương pháp tốt nhất để ngăn chặn kịch bản Phân Não (Split-Brain) trong hệ thống phân tán là gì?',
            'options': {
                'fix-1': {
                    'text': 'Triển khai giao thức đồng thuận dựa trên Túc Số Đa Số (Quorum-based Consensus) — yêu cầu phải có sự đồng thuận của đa số các nút (ví dụ 3 trên 5 nút) để bầu Leader hoặc chấp nhận lệnh ghi',
                    'feedback': 'Chính xác! Bằng cách triển khai thuật toán đồng thuận (như Raft hoặc Paxos) với số nút lẻ (tối thiểu 3 nút phân bổ hợp lý), khi mạng bị chia đôi, chỉ có phân vùng nào nắm giữ đa số nút (> 50%) mới được phép bầu Leader và ghi dữ liệu. Phân vùng thiểu số sẽ từ chối ghi, triệt tiêu hoàn toàn nguy cơ xuất hiện 2 Leader cùng lúc.'
                },
                'fix-2': {
                    'text': 'Bổ sung thêm một đường truyền mạng dự phòng giữa hai trung tâm dữ liệu để chống đứt kết nối',
                    'feedback': 'Dự phòng mạng vật lý giúp giảm thiểu sự cố đứt cáp, nhưng không thể ngăn chặn 100% rủi ro phân vùng mạng (ví dụ lỗi switch, cấu hình sai tường lửa). Bạn phải bảo vệ hệ thống ở tầng logic thuật toán.'
                },
                'fix-3': {
                    'text': 'Chỉ định vĩnh viễn một cơ sở dữ liệu làm Leader chính và không bao giờ cho phép tự động thăng cấp nếu không có can thiệp thủ công',
                    'feedback': 'Cách này ngăn được split-brain nhưng triệt tiêu hoàn toàn tính năng tự động phục hồi khi có sự cố thật sự (High Availability), khiến toàn bộ hệ thống bị tê liệt khi Leader chính gặp lỗi.'
                },
                'fix-4': {
                    'text': 'Sử dụng nhãn thời gian đồng hồ thực (Wall-clock timestamps) để tự động ghi đè bản ghi mới hơn khi mạng kết nối lại',
                    'feedback': 'Chiến lược Last-Write-Wins (LWW) dựa trên đồng hồ vật lý sẽ âm thầm xóa bỏ một trong hai lệnh ghi quan trọng và dễ bị sai lệch do độ lệch đồng hồ máy chủ (clock drift).'
                }
            }
        }
    },
    'case-05': {
        'rootCause': {
            'question': 'Điều gì đã khiến nhiều nút cùng tự xưng là Leader tại cùng một thời điểm?',
            'options': {
                'rc-4': {
                    'text': 'Mạng giữa Nút 1 và Nút 2 bị phân vùng, khiến chúng không thể nhìn thấy nhau',
                    'feedback': 'Kết nối mạng giữa các nút còn sống hoàn toàn thông suốt. Vấn đề nằm ở quy tắc kiểm phiếu bầu cử của cụm.'
                },
                'rc-1': {
                    'text': 'Leader cũ (Nút 0) bị sập đột ngột và đã gửi các thông điệp bị hỏng tới các nút khác trước khi chết',
                    'feedback': 'Nút 0 bị mất nguồn tức thì và không gửi bất kỳ thông điệp nào. Quá trình bầu cử sau đó hoàn toàn do các nút còn lại tự thực hiện.'
                },
                'rc-2': {
                    'text': 'Quy trình bầu cử không thực thi quy tắc Túc Số Đa Số Tuyệt Đối (Strict Majority Quorum) — cho phép các nút thắng cử chỉ với số phiếu thiểu số',
                    'feedback': 'Chính xác! Cụm ban đầu có 5 nút, do đó đa số tuyệt đối bắt buộc phải là ít nhất 3 phiếu (majority = floor(5/2) + 1 = 3). Tuy nhiên, hệ thống lại cho phép bất kỳ nút nào nhận được 2 phiếu bầu cũng được làm Leader. Khi Nút 1 nhận được 2 phiếu và Nút 2 cũng nhận được 2 phiếu, cả hai nút đều tuyên bố mình thắng cử, dẫn đến tình trạng hai Leader hoạt động song song.'
                },
                'rc-3': {
                    'text': 'Cả Nút 1 và Nút 2 đều bắt đầu tiến trình bầu cử tại cùng một mili-giây chính xác',
                    'feedback': 'Việc bắt đầu bầu cử cùng lúc (split vote) là bình thường trong hệ thống phân tán. Nhưng nếu có quy tắc túc số chuẩn (cần 3/5 phiếu), cả hai sẽ không đạt đa số và buộc phải thử lại với thời gian chờ ngẫu nhiên (randomized election timeout), chứ không thể cùng thắng cử.'
                }
            }
        },
        'fix': {
            'question': 'Quy trình bầu chọn Leader cần được sửa đổi như thế nào để đảm bảo tính đúng đắn?',
            'options': {
                'fix-4': {
                    'text': 'Thêm độ trễ cấu hình được sau khi Leader sập trước khi cho phép bất kỳ nút nào bắt đầu bầu cử',
                    'feedback': 'Thêm độ trễ chỉ làm chậm quá trình phục hồi hệ thống chứ không giải quyết được lỗi toán học của việc thiếu quy tắc đa số.'
                },
                'fix-2': {
                    'text': 'Sử dụng nhãn thời gian đồng hồ thực để xác định xem nút nào bắt đầu bầu cử trước một vài mili-giây',
                    'feedback': 'Đồng hồ vật lý giữa các máy chủ không bao giờ đồng bộ hoàn hảo tới mức mili-giây và không thể dùng làm trọng tài tin cậy cho việc bầu cử.'
                },
                'fix-1': {
                    'text': 'Yêu cầu phải đạt được Túc Số Đa Số Tuyệt Đối (ít nhất 3 trên 5 nút trong cụm) mới được công nhận thắng cử Leader',
                    'feedback': 'Chính xác! Trong một cụm 5 nút, một nút bắt buộc phải thu thập được tối thiểu 3 phiếu bầu (tính trên tổng quy mô cụm ban đầu). Vì không thể có hai nhóm con nào cùng có 3 nút trong tổng số 5 nút (3 + 3 = 6 > 5), việc xuất hiện 2 Leader đồng thời là điều bất khả thi về mặt toán học.'
                },
                'fix-3': {
                    'text': 'Chỉ định sẵn một nút dự phòng cố định làm Leader tiếp theo để không bao giờ phải tổ chức bầu cử',
                    'feedback': 'Nếu nút dự phòng cố định đó cũng bị chết hoặc mất kết nối cùng lúc với Leader chính, toàn bộ hệ thống sẽ bị đóng băng hoàn toàn.'
                }
            }
        }
    },
    'case-06': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ dẫn đến việc phân công điều tra vụ án bị xung đột mâu thuẫn là gì?',
            'options': {
                'rc-3': {
                    'text': 'Thanh tra Reyes và Trung sĩ Okonkwo lẽ ra phải gọi điện thoại trao đổi trước khi phân công vụ án để tránh xung đột ghi cơ sở dữ liệu',
                    'feedback': 'Quy trình phối hợp bằng miệng giữa con người không phải là giải pháp kỹ thuật tin cậy ở quy mô lớn. Hệ thống phân tán phải có trách nhiệm phát hiện và xử lý xung đột ghi đồng thời.'
                },
                'rc-1': {
                    'text': 'Độ trễ nhân bản 45 giây giữa hai máy chủ Leader là quá lớn và cần được giảm thiểu để tránh xung đột',
                    'feedback': 'Giảm độ trễ nhân bản giúp giảm tần suất xảy ra xung đột, nhưng trong mô hình Multi-Leader, bất kỳ độ trễ nào lớn hơn 0 đều có thể phát sinh xung đột nếu hai thao tác ghi diễn ra trong cùng khoảng thời gian đó.'
                },
                'rc-4': {
                    'text': 'Chiến lược giải quyết xung đột Last-Write-Wins (LWW) có lỗi phần mềm trong logic so sánh nhãn thời gian',
                    'feedback': 'Thuật toán LWW hoạt động hoàn toàn đúng theo thiết kế của nó: nó chọn bản ghi có nhãn thời gian lớn hơn. Vấn đề là bản thân chiến lược LWW là một chiến lược gây mất mát dữ liệu (lossy) âm thầm mà không hề thông báo cho người dùng.'
                },
                'rc-2': {
                    'text': 'Mô hình nhân bản Multi-Leader cho phép cả hai cơ sở dữ liệu độc lập chấp nhận thao tác ghi, khiến các lệnh ghi đồng thời vào cùng một bản ghi tạo ra xung đột cần phải được xử lý sau',
                    'feedback': 'Chính xác! Trong kiến trúc Multi-Leader, mỗi Leader nhận lệnh ghi độc lập và gửi bản sao bất đồng bộ sang các Leader khác. Khi hai đồn cùng sửa một vụ án trước khi dữ liệu kịp đồng bộ, xung đột ghi (write conflict) tất yếu xảy ra. Chiến lược Last-Write-Wins đã âm thầm xóa mất phân công của Thanh tra Reyes mà không ai hay biết — một hậu quả cực kỳ nguy hiểm cho dữ liệu pháp lý.'
                }
            }
        },
        'fix': {
            'question': 'Phương pháp tốt nhất để xử lý xung đột ghi trong hệ thống Multi-Leader này là gì?',
            'options': {
                'fix-2': {
                    'text': 'Triển khai cơ chế giải quyết xung đột ở tầng ứng dụng (Application-level Conflict Resolution) — phát hiện xung đột và hiển thị cho người có thẩm quyền phê duyệt thủ công hoặc dùng CRDT',
                    'feedback': 'Chính xác! Đối với dữ liệu nghiệp vụ quan trọng như phân công phá án, giải pháp đúng đắn là phát hiện xung đột và giữ lại cả hai phiên bản, sau đó thông báo cho người giám sát xem xét và quyết định thay vì âm thầm loại bỏ một bên. Đây là nguyên lý hoạt động của các cấu trúc dữ liệu CRDT hoặc hàm hợp nhất (merge function) tùy chỉnh.'
                },
                'fix-4': {
                    'text': 'Bổ sung cơ chế khóa phân tán toàn cầu (Distributed Global Lock) để mỗi thời điểm chỉ duy nhất một đồn được phép sửa hồ sơ vụ án',
                    'feedback': 'Khóa phân tán qua mạng giữa các trung tâm dữ liệu sẽ phá hỏng hoàn toàn lợi ích của Multi-Leader (vốn nhằm tăng tốc độ ghi cục bộ và tính sẵn sàng khi đứt mạng).'
                },
                'fix-1': {
                    'text': 'Chuyển toàn bộ hệ thống về mô hình Single-Leader duy nhất cho việc phân công vụ án',
                    'feedback': 'Chuyển về Single-Leader loại bỏ xung đột nhưng làm mất đi tính sẵn sàng cao mà Multi-Leader mang lại. Nếu đường truyền mạng tới Leader chính gặp sự cố, các đồn khác sẽ không thể giao nhiệm vụ phá án.'
                },
                'fix-3': {
                    'text': 'Tiếp tục dùng Last-Write-Wins nhưng đồng bộ đồng hồ máy chủ qua NTP chính xác hơn',
                    'feedback': 'Đồng hồ chính xác hơn chỉ giúp việc chọn bản ghi có nhãn thời gian sau chuẩn hơn, nhưng bản chất của LWW vẫn là âm thầm vứt bỏ một thao tác ghi của sĩ quan mà không có thông báo.'
                }
            }
        }
    },
    'case-07': {
        'rootCause': {
            'question': 'Nguyên nhân gốc rễ dẫn đến việc nhãn thời gian bằng chứng hiển thị thời điểm phi lý (nghiệm thu trước khi thu thập) là gì?',
            'options': {
                'rc-2': {
                    'text': 'Sự cố dịch vụ NTP dẫn đến Hiện Tượng Lệch Đồng Hồ (Clock Skew), khiến nhãn thời gian giữa các máy chủ vật lý bị sai lệch và không thể so sánh trực tiếp',
                    'feedback': 'Chính xác! Trong hệ thống phân tán, mỗi máy tính sở hữu một tinh thể thạch anh dao động riêng và đồng hồ vật lý của chúng luôn bị trôi dạt (drift). Máy chủ thu thập chạy nhanh hơn 3 phút, trong khi máy chủ phòng lab chạy chậm hơn 5 phút, tạo ra độ lệch tới 8 phút. Việc dùng đồng hồ vật lý (wall-clock time) để xác định thứ tự nhân quả giữa các máy tính độc lập là hoàn toàn thiếu tin cậy.'
                },
                'rc-3': {
                    'text': 'Cơ sở dữ liệu lưu trữ bản ghi sai thứ tự do lỗi logic trong đường truyền ghi',
                    'feedback': 'Cơ sở dữ liệu chỉ lưu trữ trung thực các giá trị nhãn thời gian mà nó nhận được. Vấn đề nằm ở chỗ các máy chủ gửi dữ liệu đã tự đóng dấu thời gian bị sai lệch do đồng hồ phần cứng của chúng.'
                },
                'rc-1': {
                    'text': 'Bằng chứng thực chất đã bị các kỹ thuật viên làm giả — nhãn thời gian vô lý chứng minh chuỗi mắt xích lưu giữ bằng chứng đã bị phá vỡ',
                    'feedback': 'Không có hành vi gian lận nào ở đây. Thứ tự các bước trong thế giới thực diễn ra hoàn toàn chuẩn xác; chỉ có đồng hồ máy chủ hiển thị sai thời gian thực do mất kết nối NTP.'
                },
                'rc-4': {
                    'text': 'Độ trễ mạng giữa máy chủ thu thập và máy chủ phòng lab khiến các sự kiện truyền tới cơ sở dữ liệu bị đảo lộn thứ tự',
                    'feedback': 'Độ trễ mạng có thể làm sự kiện đến trước hoặc sau, nhưng nhãn thời gian được đóng dấu ngay tại máy chủ nguồn. Kể cả sự kiện đến đúng thứ tự, nhãn thời gian vẫn sẽ ghi nhận lab chạy trước thu thập do đồng hồ của lab bị chậm.'
                }
            }
        },
        'fix': {
            'question': 'Cách tốt nhất để thiết lập thứ tự sự kiện tin cậy giữa các máy chủ trong hệ thống phân tán là gì?',
            'options': {
                'fix-4': {
                    'text': 'Thêm một khoảng trễ đệm tĩnh trước khi ghi nhận bất kỳ nhãn thời gian nào để bù trừ độ lệch tối đa dự kiến',
                    'feedback': 'Một độ trễ đệm tùy tiện không giải quyết được vấn đề vì độ lệch đồng hồ biến thiên liên tục theo thời gian, đồng thời làm tăng độ trễ không cần thiết cho mọi hoạt động.'
                },
                'fix-1': {
                    'text': 'Cấu hình lại máy chủ NTP và bắt buộc tất cả đồng hồ máy chủ phải đồng bộ định kỳ mỗi 30 giây',
                    'feedback': 'Sửa NTP là cần thiết nhưng chưa đủ. Giữa các chu kỳ đồng bộ, đồng hồ vẫn có thể bị trôi dạt vài mili-giây. Bạn không bao giờ có thể dựa duy nhất vào đồng hồ vật lý để chứng minh quan hệ nhân quả pháp lý.'
                },
                'fix-2': {
                    'text': 'Sử dụng Đồng Hồ Logic (Logical Clocks như Lamport Timestamps hoặc Vector Clocks) để theo dõi quan hệ nhân quả của các sự kiện qua từng nút mạng',
                    'feedback': 'Chính xác! Đồng hồ logic không phụ thuộc vào thời gian vật lý của thế giới thực. Lamport Timestamp là một bộ đếm số nguyên tăng dần theo từng sự kiện và được đính kèm vào mỗi thông điệp trao đổi giữa các máy chủ. Nếu sự kiện A gây ra sự kiện B, nhãn thời gian logic của A chắc chắn nhỏ hơn B. Đây là giải pháp tiêu chuẩn để bảo toàn chuỗi quan hệ nhân quả độc lập với độ lệch đồng hồ phần cứng.'
                },
                'fix-3': {
                    'text': 'Chỉ định một máy chủ thời gian tập trung duy nhất chịu trách nhiệm đóng dấu nhãn thời gian cho mọi sự kiện trong toàn hệ thống',
                    'feedback': 'Một máy chủ thời gian tập trung sẽ trở thành điểm lỗi đơn lẻ (SPOF) và nút thắt cổ chai hiệu năng — mọi sự kiện đều phải chờ hop mạng tới máy chủ này để lấy tem thời gian.'
                }
            }
        }
    }
}
