
INSERT INTO `accounts_hotelmanagermodel` (`id`, `hotel_id`, `user_id`) VALUES
	(1, 1, 2),
	(2, 2, 3);

-- Dumping data for table boroobia.accounts_user: ~3 rows (approximately)
INSERT INTO `accounts_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `phone`, `nid`, `birthdate`, `hotel_manager`, `profile`) VALUES
	(1, 'pbkdf2_sha256$600000$ia67TLA4OulVUYiIApkAMP$lEdZWBwmfr5pnyjiUNHSh8IVVchZjAdlcinfF1oQGlo=', '2023-11-15 10:44:03.859771', 1, 'mosjofa@5H2', '', '', 'boroobia.ir@gmail.com', 1, 1, '2023-11-15 10:43:02.881879', '', '', '', 0, ''),
	(2, 'pbkdf2_sha256$600000$5LSx6TYIcvxxlEs4qSTlmQ$2nOW5bdhxilEdAlMscPIYtVCKn/nqLGu7UvQSUmPveA=', '2023-11-15 18:17:05.000000', 0, '09129471382', '', '', '', 0, 1, '2023-11-15 15:12:45.000000', '09129471382', '1160474745', '', 0, ''),
	(3, 'pbkdf2_sha256$600000$PrASJeB9vXXfdRjbxJUxzr$cIU5Mnq0cdoTM6yGadpdh2Na7j0mpY9A3MAaIplDxX0=', '2023-11-15 17:03:24.000000', 0, '09129471383', 'رضا', 'توانگر', 'rezatavangar112@gmail.com', 0, 1, '2023-11-15 17:03:23.000000', '09129471384', '1160474745', '1402/06/02', 0, 'static/img/profiles/4bd4826bcc49156c_mHuyiH0.jpg');

INSERT INTO `hotels_city` (`id`, `name`, `faname`, `slug`) VALUES
	(1, 'Kish', 'کیش', 'kish'),
	(2, 'Mashhad', 'مشهد', 'mashhad'),
	(3, 'Isfahan', 'اصفهان', 'isfahan'),
	(4, 'Qeshm', 'قشم', 'qeshm'),
	(5, 'Shiraz', 'شیراز', 'shiraz'),
	(6, 'Tabriz', 'تبریز', 'tabriz'),
	(7, 'Tehran', 'تهران', 'tehran');

-- Dumping data for table boroobia.hotels_facility: ~0 rows (approximately)

-- Dumping data for table boroobia.hotels_hotel: ~6 rows (approximately)
INSERT INTO `hotels_hotel` (`id`, `name`, `faname`, `address`, `stars`, `likes`, `floor`, `rooms`, `distance`, `description`, `explanation`, `terms`, `slug`, `special_offer`, `online_reserve`, `boroobia_suggest`, `city_id`, `thumbnail`) VALUES
	(1, 'almas2', 'الماس 2', 'مشهد، خیابان امام رضا، امام رضا 20', 5, 0, 25, 217, 1.5, 'هتل ۵ ستاره و مجلل الماس دو از گروه هتل های الماس در اسفند ماه سال ۱۳۹۵ افتتاح شد. هتل الماس دو با ۲۱۷ اتاق با امکانات رفاهی ویژه در۲۵ طبقه با الهام از معماری خاص ملل مختلف به سبک های مختلفی چون سبک ایران باستان، سبک روسی، ترکی، رومی، آفریقایی، عربی، ایرانی، اتاق صفوی و ... موزه ای از هنر های بین المللی را به نمایش گذاشته است. هتل الماس با پرسنلی مجرب و آموزش دیده با افتخار آماده میزبانی از شما میهمانان گرامی می‌باشند.\r\nنکته قابل توجه : استعمال دخانیات در این هتل ممنوع می‌باشد.', 'نیم شارژ ورود رایگان\r\nتاریخ اعتبار از 1402/07/17 تا 1402/08/30\r\n\r\nنیم شارژ ورود رایگان ویژه میهمانان اقامت 24 صرفا جهت رزرو اتاق های یاقوت، الماس، سوئیت یک خوابه (سبک معماری تمدن ها) و اتاق دوتخته برلیان(اقامت با صبحانه) از ساعت 9 الی 14 در صورت داشتن ظرفیت و هماهنگی با واحد پشتیبانی\r\n\r\nلازم به ذکر است : نیم شارژ رایگان شامل صبحانه روز ورود نخواهد بود.\r\n\r\nخدمات ویژه هتل :\r\n\r\n- ترانسفر رفت و برگشت (فرودگاهی و راه آهن) ( لازم به ذکر است از ساعت 12 شب لغایت 6 صبح ترانسفر انجام نمی گردد.)\r\n\r\n-ترانسفر رایگان رفت به حرم\r\n\r\n-اینترنت رایگان نامحدود\r\n\r\n-استفاده از امکانات مجموعه آبی و ورزشی(استخر-سونا-جکوزی) به صورت رایگان می باشد.\r\n\r\nرزرو اتاق های VIP ( شامل اتاقهای امپریال، برلیان، سوئیت یکخوابه، هانی مون و پرزیدنت )، به همراه پذیرایی میوه و شیرینی به صورت روزانه در اتاق می باشد .\r\n\r\nپکیج تولد و سالگرد ازدواج:\r\n\r\nدر صورت اقامت میهمان در روز تولد و یا سالگرد ازدواج، از طرف هتل مراسم رایگان در نظر گرفته می شود که شامل موارد ذیل میباشد:\r\n\r\nدیزاین میز ، کیک ، کارت تبریک\r\n\r\nپذیرایی صبحانه در اتاق به صورت روم سرویس، مشمول شارژ هزینه صبحانه وپذیرایی خواهد بود.\r\n\r\nاتاق‌های برلیان ، یاقوت و اتاقهای یک تخته با توجه به ساختمان سازی فاقد ویو و دارای شیشه‌های مشجر می‌باشد.\r\n\r\nلازم به ذکر است: سوئیت هانی مون و ماه عسل و سوئیت های پرزیدنت فاقد خواب می باشند.', 'ورود و خروج: ساعت تحویل اتاق : 15:00 ساعت تخلیه اتاق: 12:00\r\nپذیرش خانم مجرد: با مدارک شناسایی معتبر\r\nصیغه نامه: با مهر برجسته محضر (فقط میهمان ایرانی)\r\nنیم بهاء: اقامت کودک زیر 5 سال (درصورت عدم استفاده از سرویس) رایگان می‌باشد و بازه سنی برای اقامت کودک بین 5 الی 10 سال (درصورت عدم استفاده از سرویس) نیم بها محاسبه می‌گردد.لازم به ذکر است : اقامت رایگان و نیم بها تنها برای یک کودک محاسبه می‌گردد.\r\nکنسلی: درخواست کنسلی رزرو از 4 لغایت 3 روز قبل از تاریخ ورود 25 درصد از مبلغ یک شب و به ازای هر اتاق بعنوان جریمه دریافت می گردد. درخواست کنسلی رزرو از 72 لغایت 48 ساعت قبل از تاریخ ورود 50 درصد از مبلغ یک شب و به ازای هر اتاق بعنوان جریمه دریافت می گردد. درخواست کنسلی رزرو از 48 تا 24 ساعت قبل از تاریخ ورود 70 درصد از مبلغ یک شب و به ازای هر اتاق بعنوان جریمه دریافت می گردد. درخواست کنسلی رزرو کمتر از 24 ساعت قبل از تاریخ ورود 100 درصد مبلغ یک شب و به ازای هر اتاق بعنوان جریمه دریافت می گردد.', 'almas2', 0, 1, 1, 2, 'static/img/200x154/image_9f8b442b-295e-4a40-b4d3-a64c10286a06.jpg'),
	(2, 'daryosh', 'داریوش', 'کیش، جنب بازار پردیسان، خیابان رودکی', 5, 0, 3, 190, 0, 'هتل داریوش کیش، یکی از بهترین هتل های کیش و معروف ترین هتل های ایران است. هتل پنج ستاره داریوش با الهام از معماری ایران باستان و تخت جمشید، در شمال شرق این جزیره قرار دارد. به همین دلیل این هتل به خودی خود، یکی از جاذبه های توریستی جزیره کیش به حساب می آید. همچنین دیگر جاهای دیدنی کیش هم از این هتل به راحتی قابل دسترسی است. این هتل، یکی از مدرن ترین و مجهز ترین هتل های کیش است. چشم انداز زیبای هتل هم از دیگر مزایای آن است. سواحل خلیج فارس به راحتی از داخل این هتل قابل مشاهده است. اقامت هتل داریوش کیش می تواند خاطره ای به یاد ماندنی و متفاوت برای میهمانان باشد. هتل داریوش کیش، امکانات تفریحی و رفاهی متنوعی دارد که لحظاتی مفرح را برای میهمانانش فراهم می کند. مجموعه آبی، دریاچه اختصاصی و زمین های ورزشی، تنها بخشی از امکانات آن است. با رزرو آنلاین از سایت اقامت ۲۴، می توانید از تخفیف رزرو هتل نیز برخوردار شوید.', 'پیشنهاد ویژه\r\nتاریخ اعتبار از 1402/08/04 تا 1402/08/30\r\n\r\nترانسفر رفت و برگشت رایگان، استفاده از خدمات سالن تنیس و استخر روباز آقایان و بانوان به صورت رایگان ویژه میهمانان اقامت 24\r\n\r\nشارژ عصرانه روزانه به صورت رایگان ویژه رزرو سوئیت های لوکس دریا، آتوسا و استدیو سوئیت رویال باغ و دریا\r\n\r\nنکته قابل توجه : میهمانان گرامی لطفا در زمان ثبت رزرو اطلاعات ترانسفر فرودگاهی ( شامل شماره پرواز، نام ایرلاین، ساعت پرواز و مبدا ) خود را وارد نمایید. در صورت عدم اعلام ترانسفر در زمان ثبت رزرو به منظور انصراف از انجام ترانسفر فرودگاهی بوده و ترانسفر انجام نمی‌پذیرد.\r\n\r\nنکته قابل توجه : ظرفیت و نرخ و سن اقامت کودک رایگان و نیم بها (درصورت عدم استفاده از سرویس) پس از استعلام از هتل اعلام می‌گردد.\r\n\r\nلازم به ذکر است : نرخ مهمان غیرایرانی متفاوت هست . لطفا قبل از ثبت درخواست رزرو خود، با پشتیانی سایت هماهنگ نمایید.\r\n\r\nنکته قابل توجه : اتاق‌های کابانا در فاصله‌ی 5 دقیقه ای از ساختمان اصلی قرار دارد.', 'ورود و خروجساعت تحویل اتاق : 15:00 ساعت تخلیه اتاق : 12:00\r\nپذیرش خانم مجردبا مدارک شناسایی معتبر\r\nصیغه نامهبا مهر برجسته محضر\r\nکنسلیکنسلی رزرو در ایام پیک و غیر پیک: با توجه به اینکه نرخ کنسلی در ایام مختلف و هتل های مختلف متفاوت می باشد، مبلغ دقیق کنسلی بعد از استعلام از هتل مشخص می گردد.\r\nشرایط خاص پذیرش کودکانظرفیت و نرخ و سن اقامت کودک رایگان و نیم بها (درصورت عدم استفاده از سرویس) پس از استعلام از هتل اعلام می‌گردد. لازم به ذکر است : اقامت رایگان و نیم بها تنها برای یک کودک محاسبه می‌گردد.\r\nپذیرش مهمان خارجینرخ میهمان خارجی متفاوت می باشد.', 'daryosh', 0, 1, 1, 2, 'static/img/200x154/1h7ka14do9.jpg'),
	(3, 'flamingo', 'فلامینگو', 'كيش، میدان امیر کبیر، بلوار دریا', 4, 0, 5, 200, 0, 'هتل فلامينگو کيش هتلی لوکس و شیک با طراحی زیبا به شکل دلفین می‌باشد که در سال ۱۳۷۶ در زمینی به مساحت ۲۴ هزار متر مربع احداث گردیده است. این هتل چهار ستاره با فضای سبز روح انگیز به همراه آبنماها و آلاچیق های زیبا در ۵ طبقه بنا و دارای ۲۰۰ باب اتاق با امکانات رفاهی مناسب می‌باشد. این مجموعه دسترسی مناسبی به مراکز خرید و تفریحی جزیره از جمله بازارهای مروارید، زیتون، ونوس، مریم و اسکله تفریحی جدید(جهت استفاده از جت اسکی، قایق های کف شیشه ای، دوچرخه سواری و...) دارد. هتل فلامینگو با پرسنلی آموزش دیده و مجرب فرصت میزبانی از شما را غنیمت شمرده و اقامتی به یادماندنی را برای شما میهمانان گرامی آرزومند اند.', 'هتل فلامينگو کيش هتلی لوکس و شیک با طراحی زیبا به شکل دلفین می‌باشد که در سال ۱۳۷۶ در زمینی به مساحت ۲۴ هزار متر مربع احداث گردیده است. این هتل چهار ستاره با فضای سبز روح انگیز به همراه آبنماها و آلاچیق های زیبا در ۵ طبقه بنا و دارای ۲۰۰ باب اتاق با امکانات رفاهی مناسب می‌باشد. این مجموعه دسترسی مناسبی به مراکز خرید و تفریحی جزیره از جمله بازارهای مروارید، زیتون، ونوس، مریم و اسکله تفریحی جدید(جهت استفاده از جت اسکی، قایق های کف شیشه ای، دوچرخه سواری و...) دارد. هتل فلامینگو با پرسنلی آموزش دیده و مجرب فرصت میزبانی از شما را غنیمت شمرده و اقامتی به یادماندنی را برای شما میهمانان گرامی آرزومند اند.\r\nلازم به ذکر است : ترانسفر فرودگاهی برای رزروهای با حداقل دو شب اقامت به بالا انجام می‌گردد.', 'ورود و خروجساعت تحویل اتاق : 14:00 ساعت تخلیه اتاق: 12:00\r\nپذیرش خانم مجردبا مدارک شناسایی معتبر\r\nصیغه نامهبا مهر برجسته محضر\r\nنیم بهاءاقامت کودک زیر 3 سال (درصورت عدم استفاده از سرویس) رایگان می‌باشد و هزینه‌ی اقامت کودک بالای 3 سال به طور کامل محاسبه می گردد.لازم به ذکر است : اقامت رایگان و نیم بها تنها برای یک کودک محاسبه می‌گردد.\r\nکنسلیکنسلی رزرو در ایام پیک و غیر پیک: با توجه به اینکه نرخ کنسلی در ایام مختلف و هتل های مختلف متفاوت می باشد، مبلغ دقیق کنسلی بعد از استعلام از هتل مشخص می گردد.', 'flamingo', 0, 1, 1, 2, 'static/img/200x154/Kish-Flamingo-hotel.jpg'),
	(4, 'parsianazadi', 'پارسیان آزادی', 'تهران، تقاطع بزرگراه چمران و یادگار امام', 5, 0, 26, 475, 0, 'هتل پنج ستاره پارسیان آزادی(هایت سابق) از مدرن‌ترین و مجلل‌ترین هتل‌های کشور می‌باشد که پس از بازسازی و تغییر دکوراسیون کامل توسط کارشناسان خارجی، بازگشایی گردید. این هتل با ۴۷۵ واحد اقامتی لوکس همراه با طراحی و دکوراسیون زیبا در ۲۶ طبقه که مشرف به سلسله جبال البرز و شهر زیبای تهران می‌باشد، بنا گردیده است. از امتیازات هتل آزادی می‌توان به دسترسی مناسب به نمایشگاه بین المللی، مرکز اجتماعات سازمان صدا و سیما، سالن اجلاس سران اسلامی و جاذبه‌های گردشگری چون مجموعه تاریخی سعد آباد، مجموعه تفریحی توچال و پارک ژوراسیک تهران اشاره کرد.\r\nهتل پارسیان آزادی با فراهم نمودن کلیه امکانات رفاهی اختصاصی، فضایی مملو از آرامش و زیبایی را برای میهمانان عزیز به ارمغان می‌آورد. از جمله امکانات این هتل می‌توان به انواع رستوران‌های ایرانی و فرنگی و فست فود و کافی‌شاپ‌های بسیار باکیفیت، گیفت شاپ، انواع سالن همایش و گردهمایی مجهز، کلوپ ورزشی و… اشاره کرد. اگرچه سابقه هتل پارسیان آزادی به دهه ۵۰ شمسی بر ‌می‌گردد، اما با یک بازسازی اساسی که در سال ۸۶ شروع شد و حدود ۴ سال به طول انجامید؛ در حال حاضر این هتل به یکی از به‌روزترین و مجهزترین هتل‌های تهران تبدیل شده است.', 'هتل پنج ستاره پارسیان آزادی(هایت سابق) از مدرن‌ترین و مجلل‌ترین هتل‌های کشور می‌باشد که پس از بازسازی و تغییر دکوراسیون کامل توسط کارشناسان خارجی، بازگشایی گردید. این هتل با ۴۷۵ واحد اقامتی لوکس همراه با طراحی و دکوراسیون زیبا در ۲۶ طبقه که مشرف به سلسله جبال البرز و شهر زیبای تهران می‌باشد، بنا گردیده است. از امتیازات هتل آزادی می‌توان به دسترسی مناسب به نمایشگاه بین المللی، مرکز اجتماعات سازمان صدا و سیما، سالن اجلاس سران اسلامی و جاذبه‌های گردشگری چون مجموعه تاریخی سعد آباد، مجموعه تفریحی توچال و پارک ژوراسیک تهران اشاره کرد.\r\nهتل پارسیان آزادی با فراهم نمودن کلیه امکانات رفاهی اختصاصی، فضایی مملو از آرامش و زیبایی را برای میهمانان عزیز به ارمغان می‌آورد. از جمله امکانات این هتل می‌توان به انواع رستوران‌های ایرانی و فرنگی و فست فود و کافی‌شاپ‌های بسیار باکیفیت، گیفت شاپ، انواع سالن همایش و گردهمایی مجهز، کلوپ ورزشی و… اشاره کرد. اگرچه سابقه هتل پارسیان آزادی به دهه ۵۰ شمسی بر ‌می‌گردد، اما با یک بازسازی اساسی که در سال ۸۶ شروع شد و حدود ۴ سال به طول انجامید؛ در حال حاضر این هتل به یکی از به‌روزترین و مجهزترین هتل‌های تهران تبدیل شده است.\r\nکنسلی رایگان\r\nتاریخ اعتبار از 1402/07/01 تا 1402/09/30\r\n\r\nکنسلی بدون جریمه ویژه میهمانان اقامت 24 تا ساعت 12 روز ورود\r\n\r\nلازم به ذکر است استخر هتل برای کودکان بالای 15 سال قابل استفاده می‌باشد.', 'ورود و خروجساعت تحویل اتاق : 14:00 ساعت تخلیه اتاق: 12:00\r\nپذیرش خانم مجردبا مدارک شناسایی معتبر (غیر بومی)\r\nصیغه نامهبا مهر برجسته محضر\r\nنیم بهاءاقامت کودک زیر 2 سال (درصورت عدم استفاده از سرویس) رایگان می‌باشد و بازه سنی برای اقامت کودک بین 2 الی 7 سال (درصورت عدم استفاده از سرویس) نیم بها محاسبه می‌گردد. لازم به ذکر است : اقامت رایگان و نیم بها تنها برای یک کودک محاسبه می‌گردد.\r\nکنسلیکنسلی رزرو در ایام پیک و غیر پیک: با توجه به اینکه نرخ کنسلی در ایام مختلف و هتل های مختلف متفاوت می باشد، مبلغ دقیق کنسلی بعد از استعلام از هتل مشخص می گردد.', 'parsianazadi', 0, 1, 1, 2, 'static/img/200x154/45-min.jpg'),
	(5, 'persianplaza', 'پرشین پلازا', 'تهران، سهروردی شمالی، چهارراه کیهان، خیابان میرزایی زینالی شرقی، پلاک ۴۲', 5, 0, 16, 96, 0, 'هتل پرشین پلازا واقع در قلب اداری و تجاری پایتخت، منطقه عباس آباد تهران در فضایی با زیر بنای ۱۳۰۰۰ متر مربع در سال ۱۳۹۷ فعالیت خود را آغاز نموده است. ساختمان این هتل مدرن در ۱۶ طبقه بنا و دارای ۹۶ باب اتاق لوکس مجهز به امکانات رفاهی مناسب می‌باشد. هتل پرشین پلازا با پرسنلی آموزش دیده و مجرب فرصت میزبانی از شما را غنیمت شمرده و اقامتی به یادماندنی را برای شما میهمانان گرامی آرزومند اند.', 'هتل پرشین پلازا واقع در قلب اداری و تجاری پایتخت، منطقه عباس آباد تهران در فضایی با زیر بنای ۱۳۰۰۰ متر مربع در سال ۱۳۹۷ فعالیت خود را آغاز نموده است. ساختمان این هتل مدرن در ۱۶ طبقه بنا و دارای ۹۶ باب اتاق لوکس مجهز به امکانات رفاهی مناسب می‌باشد. هتل پرشین پلازا با پرسنلی آموزش دیده و مجرب فرصت میزبانی از شما را غنیمت شمرده و اقامتی به یادماندنی را برای شما میهمانان گرامی آرزومند اند.\r\nکنسلی رایگان\r\nتاریخ اعتبار از 1402/07/01 تا 1402/08/30\r\n\r\nکنسلی بدون جریمه ویژه میهمانان اقامت 24 تا ساعت 12 روز ورود\r\n\r\nقوانین خاص اقامت کوتاه مدت :\r\n\r\n1- اقامت در اتاقهای ساعتی فاقد صبحانه می‌باشد.\r\n\r\n2- رزرو اتاقهای ساعتی تنها یکبار امکان پذیر است.\r\n\r\n3- حداکثر مدت استفاده از اتاقهای ساعتی 7 ساعت می‌باشد.', 'ورود و خروجساعت تحویل اتاق : 14:00 ساعت تخلیه اتاق: 12:00\r\nپذیرش خانم مجردبا مدارک شناسایی معتبر\r\nصیغه نامهبا مهر برجسته محضر\r\nنیم بهاءاقامت کودک زیر 5 سال (درصورت عدم استفاده از سرویس) رایگان می‌باشد و هزینه‌ی اقامت کودک بالای 5 سال به طور کامل محاسبه می‌گردد.لازم به ذکر است : اقامت رایگان و نیم بها تنها برای یک کودک محاسبه می‌گردد.\r\nکنسلیکنسلی رزرو در ایام پیک و غیر پیک: با توجه به اینکه نرخ کنسلی در ایام مختلف و هتل های مختلف متفاوت می باشد، مبلغ دقیق کنسلی بعد از استعلام از هتل مشخص می گردد.', 'persianplaza', 0, 1, 1, 2, 'static/img/200x154/36150.jpg'),
	(6, 'parsianesteghlal', 'پرشین استقلال', 'تهران، تقاطع بزرگراه شهيد چمران و خیابان ولی عصر، چهارراه پارک وی', 5, 0, 30, 552, 0, 'هتل استقلال تهران (رویال هیلتون سابق) بزرگترین هتل ۵ ستاره ایران در شمال تهران است که در تاریخ هشتم آذر ۱۳۴۱ افتتاح گردید. این هتل در زمینی به مساحت ۷۰ هزار متر مربع بنا شده است. هتل استقلال پارسیان تهران با قرار گرفتن در یکی از بهترین نقاط تهران، دسترسی مناسبی به طولانی ترین خیابان خاورمیانه و زیباترین خیابان پایتخت، یعنی خیابان ولیعصر دارد. همچنین این هتل تهران در نزدیکی نمایشگاه بین المللی تهران، برج میلاد، تله کابین توچال و مراکز خرید و اماکن دیدنی شهر قرار دارد. به این دلایل هتل استقلال تهران یکی از مناسب ترین انتخاب ها برای افرادی است که به هتل مسائل تجاری و کاری به تهران سفر می‌کنند. این هتل دارای دو برج شرقی و غربی با بیش از ۵۵۰ سوئیت مجلل و اتاق مجهز به امکانات رفاهی بوده و همچنین میزبان ۱۱ رستوران دائمی و فصلی است که انواع غذاهای ایرانی، فرنگی و دریایی را سرو می‌کنند. همچنین از معروف ترین وعده های هتل استقلال تهران صبحانه آن است که می‌توانید آن را امتحان کنید. از سایر امکانات هتل می‌توان به ۲ سالن ویژه‌ی همایش و مراسمات، استخر و سالن‌های ورزشی و تالار هتل استقلال تهران که میزبان عروسی های مجلل است اشاره کرد. هتل استقلال با پرسنلی مجرب فرصت میزبانی از شما را افتخار خود دانسته و اقامتی خاطره انگیز را برای شما به ارمغان خواهد آورد.\r\nلازم به ذکر است استخر هتل برای افراد بالای ۱۵ سال قابل استفاده است.', 'هتل استقلال تهران (رویال هیلتون سابق) بزرگترین هتل ۵ ستاره ایران در شمال تهران است که در تاریخ هشتم آذر ۱۳۴۱ افتتاح گردید. این هتل در زمینی به مساحت ۷۰ هزار متر مربع بنا شده است. هتل استقلال پارسیان تهران با قرار گرفتن در یکی از بهترین نقاط تهران، دسترسی مناسبی به طولانی ترین خیابان خاورمیانه و زیباترین خیابان پایتخت، یعنی خیابان ولیعصر دارد. همچنین این هتل تهران در نزدیکی نمایشگاه بین المللی تهران، برج میلاد، تله کابین توچال و مراکز خرید و اماکن دیدنی شهر قرار دارد. به این دلایل هتل استقلال تهران یکی از مناسب ترین انتخاب ها برای افرادی است که به هتل مسائل تجاری و کاری به تهران سفر می‌کنند. این هتل دارای دو برج شرقی و غربی با بیش از ۵۵۰ سوئیت مجلل و اتاق مجهز به امکانات رفاهی بوده و همچنین میزبان ۱۱ رستوران دائمی و فصلی است که انواع غذاهای ایرانی، فرنگی و دریایی را سرو می‌کنند. همچنین از معروف ترین وعده های هتل استقلال تهران صبحانه آن است که می‌توانید آن را امتحان کنید. از سایر امکانات هتل می‌توان به ۲ سالن ویژه‌ی همایش و مراسمات، استخر و سالن‌های ورزشی و تالار هتل استقلال تهران که میزبان عروسی های مجلل است اشاره کرد. هتل استقلال با پرسنلی مجرب فرصت میزبانی از شما را افتخار خود دانسته و اقامتی خاطره انگیز را برای شما به ارمغان خواهد آورد.\r\nلازم به ذکر است استخر هتل برای افراد بالای ۱۵ سال قابل استفاده است.\r\nکنسلی رایگان\r\nتاریخ اعتبار از 1402/08/02 تا 1402/09/30\r\n\r\nکنسلی بدون جریمه ویژه میهمانان اقامت 24 تا 24 ساعت قبل از ورود', 'ورود و خروجساعت تحویل اتاق : 14:00 ساعت تخلیه اتاق: 12:00\r\nپذیرش خانم مجردبا مدارک شناسایی معتبر\r\nصیغه نامهبا مهر برجسته محضر\r\nنیم بهاءاقامت کودک زیر 2 سال (درصورت عدم استفاده از سرویس) رایگان می‌باشد و بازه سنی برای اقامت کودک بین 2 الی 7 سال (درصورت عدم استفاده از سرویس) نیم بها محاسبه می‌گردد. لازم به ذکر است : اقامت رایگان و نیم بها تنها برای یک کودک محاسبه می‌گردد.\r\nکنسلیکنسلی رزرو در ایام پیک و غیر پیک: با توجه به اینکه نرخ کنسلی در ایام مختلف و هتل های مختلف متفاوت می باشد، مبلغ دقیق کنسلی بعد از استعلام از هتل مشخص می گردد.', 'parsianesteghlal', 0, 1, 1, 7, 'static/img/200x154/هتل-استقلال-تهران.jpg');

-- Dumping data for table boroobia.hotels_hotelimage: ~6 rows (approximately)
INSERT INTO `hotels_hotelimage` (`id`, `hotel_id`, `image_id`) VALUES
	(1, 1, 1),
	(2, 2, 2),
	(3, 3, 3),
	(4, 4, 4),
	(5, 5, 5),
	(6, 6, 6);

-- Dumping data for table boroobia.hotels_hotel_facilities: ~0 rows (approximately)

-- Dumping data for table boroobia.hotels_image: ~6 rows (approximately)
INSERT INTO `hotels_image` (`id`, `name`, `file`) VALUES
	(1, 'هتل الماس 2', 'static/img/820x550/image_9f8b442b-295e-4a40-b4d3-a64c10286a06.jpg'),
	(2, 'داریوش کیش', 'static/img/820x550/1h7ka14do9.jpg'),
	(3, 'هتل فلامینگو کیش', 'static/img/820x550/Kish-Flamingo-hotel.jpg'),
	(4, 'هتل پارسیان آزادی تهران', 'static/img/820x550/45-min.jpg'),
	(5, 'هتل پرشین پلازا تهران', 'static/img/820x550/36150.jpg'),
	(6, 'هتل پرشین استقلال تهران', 'static/img/820x550/هتل-استقلال-تهران.jpg');

