# Kendi Yapay Zeka Ekibimi Kurdum. Ben Kod Yazmıyorum.

- URL: https://www.youtube.com/watch?v=MFqtKpzttGA
- Channel: Avenox
- Language: tr
- Type: manual

---

Yapay zekada kendini ileriye atmak isteyen herkes bir yerden sonra orkestrasyon öğrenmek zorunda kalıyor.
Yani birden fazla yapay zeka modelini aynı anda tek bir parça gibi yönetebilmeyi anlaması lazım.
Ben de bu videoda kendimin birden fazla yapay zeka agentini aynı projede nasıl çalıştırdığımı,
çalıştırırken nelere dikkat ettiğimi, nelere dikkat etmediğimi bunları göstermek istedim.
Video içerisinde ara ara da Claude Code'a geri döneceğiz.
Claude Code'da örnekleriyle göstereceğim. Yavaştan başlayalım. Benim için en önemli konu şu aslında.
Ben üstte bir tane agent koyarım arkadaşlar.
Altına diğer agentları veririm. Benim ana konuştuğum agent kod yazmaz genel olarak.
Benim konuştuğum agent alttaki diğer agentları yönetir.
Bu Claude olabilir, Codex olabilir. Benim tüketimimde bu ikisi var genel olarak. Ana koyduğum agent genelde Claude modeli oluyor.
Özellikle Opus 5.5 ile beraber bu olay çok farklı bir seviyeye geldi.
Aşağıdaki agentlarda normalde Codex agentları oluyordu.
Codex'teki limitimle dengeleyebilmek için. Ama artık dürüst olmak gerekirse genel olarak onları da Opus yapıyorum.
Limitlerime bağlı olarak. Bakın aslında orkestre ediyor.
Hepsini o yönetiyor. Orkestrasyondan kastımız bu arkadaşlar. Biz kod yazmıyoruz. Ben toplum 2000 tane agent'a iş vermişim. Bunlar 1653 tane alt agent açmış.
Bu alt agent'lar çalışmış aslında. Bak Codex tarafında çalışan alt agent. Yani ben kod yazdırmıyorum aslında. Ben üsttekiyle sanki bir patronmuş gibi konuşuyorum.
O alttakileri yönetiyor. Bir de mesela örneğini söyleyeyim. Bakın komutu kopyalıyorum. Terminalde aç diyeceğim şimdi. Şimdi bakın girdikten sonra prompt'u kopyalıyorum.
Prompt basit bir şey aslında. Örnek dosyayı koydum. Hiçbirini kendi okuma diyorum. Her birini alt agent yap. Hepsi aynı anda çalışsın. Bakın sadece dosyanın varlığını doğruladı.
Kendisi okumadı. Bunların her birini alt agent yolladı. Yani aslında alt agent yollamak bu kadar basit arkadaşlar.
Normal dille yolluyorsunuz. Yani özel bir şey yapmanıza gerek yok.
Herhangi bir hedef için şu kadar agent yolla.
Bu kadar agent yolla. Biz mesela 5 farklı konu almak için istedik.
Örnek dinleleri istedik. Sonra tek satırla kaç token harcadığını filan öğrenmek istedik.
Şimdi burada bir ton agent çalıştırıyor farkındaysanız.
Şu an 9 farklı agent var. Burada mantık şu. Alttaki agentler işi yapacaklar. Bu alttaki agentler işini bitirdikçe üstteki agent'a haber verecekler.
Üstteki agent'a sadece bu özet gidecek aslında.
Rapora hazırlamış oldu. Ve gerekli verileri de almış oldu.
Yaklaşık 61.000 token kendi contextinden gitmiş.
Alttaki agent'lardaysa 311.000 token gitmiş.
Bakın 311.000. Bu ne demek? Aslında biz 311.000 token'lık veri işledik.
Ama üstteki agent'ın sadece 61.000 token'a gitti.
Ki bunun birçok kısmı aslında sistem promptu vs. vs.
Yani toplasak belki 10-15.000 token gelmemiştir.
Bu yüzden aslında bunu yapıyoruz. Hem işleri hızlandırıyoruz alt agent'larla.
Hem de üst agent'ın bağlamının dolmasını engelliyoruz arkadaşlar.
Modelin kafası karışmadan çalışabilmemizi sağlıyor.
Amacı bu. Bir sonraki aşamada ise kendi loglarımı saydım.
Bakalım loglarım bana ne diyor. Buna baktık. Ben genel olarak Claude agent'larıyla orkestrasyon yapıyorum.
Codex agent'larıyla o denli bir orkestrasyon yapmıyorum.
Codex agent'larını alt agent olarak gene Claude'ınki kullanıyorum.
Bunda nedeni şu. Codex'te yapamayacağınız anlamına gelmiyor. Durduk yere kafanız karışmasın. Codex'te de yapabilirsiniz. Bununla alakalı problem yok. Ben genelde Claude agent'larıyla çalışmaktan daha çok zevk aldığım için.
Codex'te de aynı mantık. Nasıl biz Claude'da alt agent çalıştır diyorduk.
Codex'te de aynısını diyoruz. Ek bir şey yapmamıza gerek yok. Gereksiz yere karıştırıyorsunuz. Özel sistemler oluşturmaya çalışıyorsunuz. Ancak çoğu durumda oraya verdiğiniz emek gerçekten hem durduk yere olayı karıştırıyor arkadaşlar.
Hem de verimliliği düşürüyor. Özel her bir alt agent'a özel sistem prompt yazmak, özel karakter koymak yok.
Sen şu mimarsın, sen yok. Kodu şu inceleceksin falan. Bunlara gerek yok artık. Gerek yok. Zaten üstteki agent'ımız alttaki agent'larımıza prompt yazıyorlar.
Bunları yapmayın arkadaşlar. Gereksiz yere kendiniz yoruyorsunuz. Bakın mesela özellikle Eylül ayında bayağı Claude Code'a abanmışım.
Bu da mesela bu süreçteki rekorları girmiş.
Tek seferde aynı anda alt agent tavanı 20 olmuş.
Tek workflow'da 228 agent'ı aynı anda çalıştırmışım.
Bakın gördüğünüz üzere ise alttaki agent'a neredeyse her zaman Opus vermişim.
Arkadaşlar şunu unutmayın. Şef işçilik yapmaz. Üstteki agent'ımız işçilik yapmayacak.
Bununla alakalı benim orkestrator skill'lerim var kitapta.
Bunlara bakabilirsiniz. Eğer biz üstteki agent'tan kendisinin işçilik yapmasını istersek güzel bir iş çıkartmamız çok zaman alır.
Kalitemiz çok düşer. Agent'ın sürekli context bilinimi dolar.
Genel işi takip edemez. Onun yerine alttaki agent'ları farklı farklı yerlere yollarsa ne oluyor biliyor musunuz arkadaşlar?
Atıyorum siz 5 farklı yönde iş yapıyorsunuz. Üstteki agent'ımız bunların hepsini hem kafada tutup ona göre plan yapabiliyor.
Hem contextte dolmadığı için daha uzun süre aynı agent ile çalışabiliyoruz.
Hem de paralelleştirdiğimiz için işi hızlandırabiliyoruz.
Ben mesela diyorum bakın artık üstteki agent'a asla monel kod yazdırmıyorum.
Hep alt, hep alt. Örneğini de gösteriyorum şimdi.
Dağıttınız diyelim. contextte şefin %8 doluydu.
Bakın bunlar iş yapıyor. 11 tane agent var. Bakın %32'ye çıktı. Bunlar gerçek log'lardan. Gerçek log. Gerçek log da ne oldu? 8'den 32'ye çıktı. Biz 11 tane alt agent kullandık.
Peki bunu yapmasaydık ne olurdu? Bakın 11 tane alt agent kullanmak yerine kendimiz yapıyoruz.
Daha işi bitirmeden contextte doldu.
Ne oldu? Compaction yedi. İş sarpa sarmaya başladı. Ve 2 tane üst modelin, daha pahalı modelin 2 contextte doldurmuş oldu.
Hem harcanan limit daha fazla çoğu çünkü üstteki modele işi yaptırıyoruz.
Pahalı modele. Bir anlam ifade etmiyor. Bunun yerine ben şu anda üstteki agent'a Opus, alttakini de Opus yapıyorum.
Diyorsanız ki ben bunu istemiyorum. Üsttekini Opus, alttakini Sonnet yapabilirsiniz.
Şu an Fable'ı orkestrator yapmaya gerek yok.
Opus'a çok güzel bir güncelleme geldi. İleride tekrar bakarız Fable'a güncelleme geldiğinde.
Bence şu an en iyisi Opus'un üst agent olması.
Peki diyeceksin taha her şey güzel.
Sen de Codex'te ne yapayım o zaman? Codex'te limitin bu olsa üst agent'ı astra yap şu an altı sol yap.
Limitin bu olsa ki muhtemelen değildir. Çünkü 20x pakette bile şu an bu kurtarmıyor arkadaşlar.
Kötü yani problemli. Öbür türlü üstteki agent'ı sol alttakini de yapabilirsin.
Çekilmeyin deneyin. Birkaç farklı format deneyin. Limitlerinize bağlı olarak. Codex'te de aynı şekilde. Bakın görüyor musunuz? İki tane alt agent yollamasını istedim. İkisi de cevabını verdi. Yani Codex'te de aynı şekilde. Ek bir şey yapmanıza gerek yok. Agent'ları nasıl yollayacağını kendiniz söyleyebilirsiniz.
Bunu takip edecektir. Bunu dinleyecektir agent'lar. Toplam mesela 24-25 Eylül gecesinde alt agent'larımla üst agent'ıma baktığımızda
şefin toplam tool call'daki payı %2.7.
Diğerleri 4330. Bakın aradaki farkı bakın. 40'ta birini sadece üstteki benim konuştuğumu yapıyor.
Onun yerine alttakileri orkestre ediyor. Bakın kesinlikle tavsiye ediyorum. Her işi için farklı tabii ki çalgı ihtiyacımız var.
Her işi aynı şekilde yapamıyorum ben de. Codex'te Luna ucuz context arama vs.
Toplu tarama vs. bunlar için çok güzel.
Ben Sonnet'i kendi kadromda şu an çalıştırmıyorum.
Bazı durumlarda çok nadiren kullanmaya başladım Sonnet 5 ile beraber ve indirimin kalıcı
haline gelmesiyle beraber. Ancak şimdilik çok gerek duymuyorum.
Çünkü zaten o pus fiyat olarak fena değil. Sonnet biraz gereksiz kalıyor bence.
Onun dışında ise Codex Astra ise gerçekten çok büyük bir model ve çok pahalı bir model.
Ona göre maksimum ikinci görüş veya çok aşırı zor işler vs. bunlar da kullanıyorum.
Bakın atıyorum burada farklı farklı görevler var.
Bunları kendimiz seçebiliriz. Ben direkt hızlıca geçirmek için şefi dağıtsın diyorum.
Bakın farklı farklı görevleri farklı farklı modellere dağıttı.
Ne yaptı mesela? Opta log taraması ve toplu basit işi attı. Codex'e hassas iş ve görsel üretimi ve ikinci görüşü attı.
Şimdi şu dönemde ne oluyor arkadaşlar? Ben size söyleyeyim. Şu anda görsel kısmında tabii ki Codex modelleri lazım.
Bu benim kendi logumda olan şeyi kopyalıdı bu arada.
Yani o gün o tarzda onu yapmışım. Ben genellikle mesela artık Opus'u kullanıyorum show iş için.
Altına Sonnet agent'ı verebilirim hızlıca context toplaması için.
Ancak bu kadar. Bakın 7 Eylül'de mesela tekrar yolluyorum.
7 Eylül'de Sonnet agent'larını da kullanmışız.
Bakın 7 Eylül'de mimari kararı Fable'a vermişim.
6 Eylül'de Opus yapmışım log tarama ve basit işler için.
Codex artı hasta re, hassas iş vs. bunları yapmışım.
Sonnet'i çok az kullanmışım. Mesela Ağustos'ta ise genel olarak Sonnetini daha aktif kullanmışım.
Şu an mesela bugüne dönüyorum. Bakın bugün Full Opus ve Astra.
Niye Astra? Genellikle görsel üretim vs. bunun için. Ek olarak da Astra'daki limitlerin bitsin diye bu kadar.
Ancak şu an Full Opus. Opus gerçekten güzel olmuş. Onu söyleyeyim. Şimdi bakın bu Orchestration işini yapıyorken.
Aynı dosyaya, aynı yöne, aynı görevlere vs. birden fazla agent yollamak doğru değildir.
Doğru olmaz. Bunun yerine sınırları çizmeniz lazım.
Yani ne yapacaksınız? Şu tarafı biri yapacak, bu tarafı diğeri yapacak gibisinden.
Aynı dosya üzerinde çalışırlarsa olmaz.
Peki bunu şu an artık kendimizin yapmasına çok gerek yok.
O kadar zor değil. Biz buna göre skill yazdığımızda sadece desek ki biz sen alt agentları yönetirken dikkat et.
Buna dikkat et. Aynı kısma yollama. Güzel ayır dediğimizde bizim üstteki agentimiz zaten bunu yapacaktır arkadaşlar.
Ne yapıyor mesela burada bakın. Sınır çiziyor değil mi? Her agent farklı bir alanda çalışıyor. Aynı bölgede çalışıp birbirlerinin işini baltalamıyorlar.
Öbür türlü bakın şuradaki olay gibi olur.
Aynı bölgede çalışıp birbirinin işini baltalarlar.
Bunu yapmayın. Sınırları düzgün çizmezsek olmaz.
Bakın görüyor musunuz? Herkesin sınırı belli. Ortak dosyalar belli. Ortak dosyalardakiler onunla çalışacak.
Diğerlerinde diğeri çalışacak. Öbür türlü herkes kendi masasında farklı şekilde çalıştığında olmaz.
Bakın çakışma var. Patlıyor. Görüyor musunuz? Bunu nasıl çözebilirsiniz? Bir. Sahipliği bölersiniz ilk başta. Prompt bazında vesaire böler. Onun dışında ek olarak ayrı worktreelerde çalıştırırsınız.
Böyle yaptığınızdaysa tabi worktreeler bittiğinde belli bir çakışma olursa onu mergelemeniz, çözmeniz gerekebiliyor.
Ya bazı durumlarda güzel oluyor arkadaşlar. Ben mesela çok kullanıyorum onu söyleyeyim. Sahipliği bölmek de aynı şekilde. Sırayla yapmak çakışma olmaz ama o zaman da biraz daha paralel çalışmadan kaybetmiş oluyor.
Zaten üstteki agentımız öyle görevler verecek ki bakın mesela buna dokunmaya çalıştığı anda izin vermeyecek agent'a.
İzin vermeyecekten kastım şu. Zaten buna dokunma dediği için agent buna saygı duyacaktır.
Şu anki modeller. Üst seviye modeller yapacaktır. Bakın demin gösterdim. Dedim ki bunu okuma dedim. Okumadı. Sadece dosyayı listeledim. Fark ettiyseniz. Saygı duyuyorlar. Bakın deminki olayı kopyaladım ve örneğini yaptırıyorum.
Low level'da açtım. Çünkü kolay görevler bunlar. Çok beklememize gerek yok. Üç tane alt agent dedim. Ayrı ayrı yerlerde çalışsınlar. Her bir görevlerini ayır. Ona göre yapsınlar. Bu kadar. Ona göre hızlıca planını yaptı ve onlara görevler dağıttı.
Görevler ne? Projeyi söylüyor. Hedefini söylüyor. Yapılması gerekeni söylüyor. Bu kadar. Ya bir problem yok zaten. Hızlıca yapabilir bunu. Niye hızlıca yapabilir? Bir sıkıntı yok ki. Nerede sıkıntı yaşayacak bunu? Zaten görev çok net ve basit. Değil mi? Her şey basit. Agent'lar işini bitirdi. Hepsi kendi bölümünü yapmış. Git statüsten kontrol edebiliyoruz.
Değiştirmemesi gereken dosyaları değiştirmemişler.
Her biri kendi görevinde ayrı ayrı yapmış. Bu değişiklikleri de yapmışlar. Yani herhangi bir problem patlayan herhangi bir şey yok.
Her biri kendi alanıyla ilgilenmesine rağmen aynı dosyada çalışsa bile bir problem olmamış.
Olmaz da zaten. Genelde zaten alttaki agent'lar da arkadaşlar şey yapmıyorlar.
Çok uzun mesajları atmıyorlar.
Genel olarak şefin okuyacağı, üstteki agent'ın okuyacağı kısa raporlar atıyorlar.
Ona göre yapıyorlar. Süreci aslında birçoğunuz kafanızda karıştırıyorsunuz.
Bu kadar karıştırmanız gereken hiçbir şey yok. Bu dediğim şeylere uyduğunuz sürece. Genel olarak başta nasıl çalışması gerektiği, bunun üzerine skill'leri oluştururum veya CLAUDE.md'yi artık ne yapacaksanız.
Şunu deyin. Bende mesela protokolüm var. Bunun GitHub'da skill'im var. O dönem ne yapıyormuşum? Fable'ı sub-agent olarak nadiren kullan demişim.
Çok gerekmedikçe özellikle söylemediğim sürece.
Sonnet ve IQ agent'ı ben kullanmak istemiyorum.
Şu an demişim ki bakın context toplama işi için Opus'u kullan.
Gevşek brief var. Yani çok detaylı görev verme. Çok detaylı görev vermene gerek yok. Opus çok zeki. Sen çok detaylı görev verirsen aptallaştırırsın modeli.
Altı cint olarak Opus demişim gene. Mesela execution işlerinde gene Opus demişim.
Peki zor hassas execution böyle hassas işler isteyen şeylerde Codex Astra demiştim.
Ama şundan dolayı onu da söyleyeyim. Normalde ben bunu Codex Sol'la yapıyordum. O dönem Codex Astra'nın limitleri gerçekten çok iyiydi.
Bende çok fazla limit vardı. O anlık Astra'ya çekmiştim. Ama bunu Codex Sol gibi düşünebilirsiniz. Spektör, sentiz vesaire yargıyı bunları da Fable'a bırakmıştım.
Artık benim gözümde durum daha basitleşti.
Artık bu da Opus. Yani şu an mesela Claude kısmı tamamı Opus.
Codex kısmını belki sola döndürebilirim.
Bu kadar. Yani aslında tüm süreci bir katman aşağıya indiriyorum.
Niye? Artık modeller çok zekileştiği için. Bu kadar pahalı modellere ihtiyacımız yok.
Gerçekten işini layıkıyla yapabiliyorlar şu anki modeller.
Tabii ki belli test standartları koymamız da güzel oluyor.
Eğer testler mantıklı olmazsa test geçer.
Ama sahte bir test olmuş olur. Yolladım dedim ki burada bir rapor var.
Testlerden geçiyor. Ama bir hata var. Alt agent yolla o hatayı yakalayan bir test eklesin.
Sonra ayrı bir incelemeci agent aç. O da şunu yapsın. Düzeltmeyi geri alsın. Gerekli şeyleri yapsın vs. Normalde bu kadar kasmalı. Gerek yok. Tamam. Benim size tavsiyem şudur. Ben bunları size örnek olarak arka dönen süreci anlatmak için gösteriyorum.
Benim size tavsiyem şu. Siz her zaman üstteki agentla aranızda bir iletişim alı olsun.
Üstteki agentla şunu konuşun. Deyin ki. Ben genel olarak şunlara şunlara şunlara dikkat ediyorum.
Toplarken ben bunu Sonnet agentıyla toplamak istiyorum.
Bunları söyleyin. Ben bazı işleri Codex'e yığmak istiyorum.
O işler şu tarz işler. Örneğin çok büyük bir veri var. Ben bunu unuyancı ile yapmak istiyorum ki ucuz ol.
Gibi gibi. Bu tarz. Ayırın işleri ve modele anlatın. Aklınızdaki olay nedir? Buna göre bir skill oluşturur. Ve o skill'e göre üstteki agent zaten her şeyi halledecektir.
Siz gereksiz yere kafanızı yormayın. O kısımla uğraşmayın. Bırakın artık model orkestrasyon kısmını da alttaki modelleri yönetme kısmını da üstteki model yapsın.
Tek olayınız şu olsun. Siz üstteki modeller bir arkadaş gibi bir ortak gibi konuşun.
O üstteki model işi yapmaya devam etsin.
Arkada dönen pratikleri göstermek için anlatıyorum.
Aslında mesela bu dediğimiz şeyleri üstteki agentınız zaten yapacak.
Eğer düzgün bir şekilde kendinizi ifade ettiyseniz bir problem olmaz.
Ve şunu da söyleyeyim. Özel bir orkestrasyon tool'una vs. bir şeye ihtiyacınız yok arkadaşlar.
Gerek yok. Oraya verdiğiniz emek emin olun. Alacağınız sonuca değmiyor. Değiyor olsa tamam derim ben de kullanırım.
Gerek yok. Adam akıllı commit mantığı. Adam akıllı rapor mantığı. Adam akıllı bir şey patladığında onun ne yapılacak?
Onun mantığı. Work trailer kurma. Bunları yapmazsak böyle patlar.
Bir şey patladığında da iş gider.
Niye? Commit atmıyor agentlar. Adam akıllı sürekli sık sık commit atmıyor.
Ben normalde ne diyorum? Kendi agentlarımda diyorum ki. Eğer belli bir ilerlemeden sonra artık o işe bağlı olarak alttaki agentlar commitini atsın.
Gerekirse ayrı bir branşle çalışırsınız.
Problem olmaz. Sadece o iş kaybolmasın arkadaşlar. İş kaybolmasın. İş yarıda bitse bile problem olmasın.
Agent kolay kolay takip edebilsin. Kitabı kullanın. Kullanmak zorundasınız. Sonra ben genel olarak bu tarz işlerde bir tane örnek bir rapor çıkarttırırım.
Bu rapora her agent belli notlarını alır.
Her birini atıyorum altında dosyaları olur. Her bir o alttaki dosyaya kendi notlarını alır.
Başka bir agent da onları derler. Demek istediğim şey şu. Örneğin ben 5 farklı agent yolladım. Son bir haftaki commitlerimi incelemesi için örneğin. Bu 5 tane agent'a derim ki bulduğun şeyleri ara ara incelediğin aralığı vs. bunları şuraya yaz.
Diğeri de kendi aralığını yazar. Bu sayede aynı tarafa bakmazlar sürekli.
Aralarında kendileri koordine olabilirler.
Bizim sürekli manuel uğraşmamıza gerek yok.
Agentler birbirlerini koordine edecektir zaten. Onun dışında artık bunu içerisine soktular modellerin.
Çoğu kendisi otomatik yapıyor. Bir agent eğer patlarsa bir sıkıntı olduğu, API sıkıntısı olduğu, internet artık ne olursa bir problem yaşarsa üstteki agentimiz ona mesaj atıyor ve devam ettiriyor.
Ecolact'te worktreeleri de kullanabilirsiniz. Ben bol bol kullanıyorum. Çok büyük değişiklikler yapacaksınız. Farklı farklı alanlarda çok fazla iş yapacaksınız vs.
worktreelerle çalışın. İşleri bitsin. Ondan sonra o worktreeleri birleştirirsiniz.
O worktreeler biraz daha şunun gibi düşünebilirsiniz.
Her biri kendi versiyonunda çalışıyor gibi düşünebilirsiniz.
Her biri kendi alanında çalışıyor. Birinin yaptığı iş diğerini bozmuyor. En son biz bunları toplu bir şekilde ana kodumuza alıyoruz.
Bu ana kodumuzu alırken atıyorum benzer diğerlerde değişiklikler olduysa üstteki agentimiz bunları tek tek inceliyor.
Toplu bir şekilde onu düzeltiyor. Bir problem olmuyor. Bu sayede atıyorum 20-25 agentin yaptığı işi toplu bir şekilde problem çıkmadan toplu bir şekilde inceleyerek geçirebiliyoruz.
Bakın bunları açıkken olan olaya bakın şimdi.
Mesela patladı kaldığı yerden devam ediyor.
Niye çünkü worktreedeydi kaldığı yerden devam ediyor.
Bu kaldığı yerden devam ediyor. Tool hatası oldu kaldığı yerden devam ediyor.
Bilgisayar kapandı bak tekrar açısından kaldığı yerden devam ettiriyor üstteki şefimiz.
Hiçbir problem olmadan tüm süreç tamamlanmış oluyor.
Böyle çalıştığınız sürece herhangi bir problem olmaz.
Bakın kaybolan iş 0 dakika. Ya bunlar benim gerçek döngülerim. Görüyor musun mesela? A hatası yaşamışım. 87 dakika boyunca kapalı olmuş. Ne olmuş? Sonra devam ettirmişim. Kaldığımız yerden devam etmişiz. Herhangi bir problem olmamış. Önceki turlarda hiçbir şey kaybolmuyor. Ben bu tarz orkestrasyon yapıyorum. Özel bir tool kullanmıyorum. Özel bir sistem kullanmıyorum. Sadece arkadaki mantığı bir kere kafama oturttuğum için bu mantığa göre çalıştırıyorum hepsini.
Bunu sürekli çalıştırınca da problem olmuyor.
Tabii ki belli problemler üst üste geliyorsa arkadaşlar onu kurallarda çevirin.
Skill olabilir. Farklı farklı agents MD olabilir. CLAUDE.md olabilir. Bak mesela aynı atayı sürekli almışız. Kaç tane tur oldu? Çevirdim kurala. Bir daha almayız. Niye artık model bunu biliyor? Görüyor musun? Veya çevirdim kurala. Bakın artık model bunu biliyor. Aynı şekil. Yani sürekli aynı problemleri yaşıyorsanız bunu ya skill'e döndürün ya CLAUDE.md'ye ekleyin.
İnada gerek yok. Çok inat yapıyorsunuz. Her şeyi manuel yapmayın. Şu an dediğim gibi artık ben dümeni değiştirdim.
Eski versiyon değil. Eskiden daha karışıktı. Şu an aslında çok kolay. Aşırı kolay. Hem chef aynı model hem alt agent aynı model.
Bu ne zamana kadar devam edecek onu da söyleyeyim.
Fable ve Sonnet modelleri çıkana kadar devam eder.
Şu an mesela Sonnet 5.5 gelse muhtemelen bir kademe daha aşağı inirim.
Opus'u orkestrasyon için kullanırım.
Sonnet'i iş yapmak için kullanırım. Çünkü gerçekten bu 5.5 seviyesi farklı bir seviye olmuş.
Benim bu seviyede bir zekaya birçok iş işin yok aslında.
Benim ihtiyacım şu aslında. Üstte çok zeki bir şef olsun. Bu üstteki şef kendi karar versin.
Süreci de kendisi yönetsin. Alttakiler de belli bir seviyenin üstü zekada sahip olsun.
Bu işleri yapabilsin. Bundan dolayı ek olarak da bu dediğim şeyleri eğer limitiniz bolsa benzer mantık olarak ultra kod da yapıyor arkada zaten.
Siz mesela ultra kod çalıştırdığınızda ilk yapacağı şey şudur.
Ortak bir kod yazar. Bu kod aslında hepsinin beraber çalıştığı bir sözleşme gibidir.
Yani bizim yaptığımız şeyin benzer mantıklarını Claude Code da kendi içerisine getiriyor zaten.
Biz mesela yeni bir adet getirmiyoruz aslında.
Biz en güzel pratikleri kendi alanımızda uygulamaya çalışıyoruz.
Bu işe kafa yoğurmuş insanların zamanla geleceği yer hepsi aynı.
Bakın ultra kod olarak yolluyorum size bir şey göstermek için.
Ve ek olarak bakın şunu da yapabiliyorsunuz arkadaşlar.
Ultra kod yaptınız ya. Örneğin siz mesela Opus ile ultra kod yapıyorsunuz.
Çok fazla agent çalıştıracak değil mi? Bu agentların her birinin Opus olmasına gerek yok.
O maliyeti karşılamanıza da gerek yok.
Alt agentlar Sonnet olsun bu arada.
Bakın bunu derseniz sadece ultra kod çalıştırıyorsa bile alt agentların hangisi olacağına gene kendisi karar verebiliyor.
Bu ultra kodun olayı şu.
Bir tane ortak kod yazıyor. Bir tane ortak sözleşme yazıyor. Bu sözleşme etrafında çalışıyor tüm agentlar.
Yani aslında bir kod çalıştırıyor tüm sözleşmeyi.
Benim Claude Codea sıfırdan başlama videomda bu da var.
Bakın workflow başlattı. Yaklaşık 16 tane agent yolladı.
Toplam 500 bin token'dan fazla 7 şimdiden.
Workflowlar böyledir arkadaşlar. Baya token yerler. Ben size burada içerikte gösterebilmek için bol bol kullanıyorum.
Mantığını anlayın diye. Gerçek hayatta o kadar aktif kullanmanıza gerek yok.
Mantığı güzel. Ben beğeniyorum workflowları. Ancak limitinizin bol olduğu dönemlerde yapın sadece.
Limitiniz yenilenmeye yakındır. Boş token'ınız vardır vs. Toplu işin üzerinden geçmek istiyorsunuzdur. Yaparsınız. Onun dışında her zaman yapmanıza gerek yok.
Biraz abartı olabilir. Limitlerinizi gerçekten bitirebilir yani.
Bakın görüyor musunuz? Workflowlarda iki farklı workflow sistemi kurmuş.
Biri buluyor diğeri doğruluyor diğerinin yaptığı işi.
Yani mantık bundan ibaret. Ama size daha iyisini göstereyim. Fark ettiyseniz hep Sonnet agent.
Yani benim dediğim şeye uyuyor. Orkestrasyonu ayrı bir uygulamayla ayrı bir şeyle vs. yapmamıza gerek yok arkadaşlar.
Kendisi yapacaktır. Artık sistemler çok geliştiler. Diğer taraf devam ederken ben de arkaya dönen işlerimi göstereyim.
Dünden beri bu devam ediyor. Yani yaklaşık bir 15-20 saattir oluyordur.
Yayına başlamıştık. Görmüşsünüzdür. Çok ciddi bir yapılması gereken iş var diyeyim.
Çok fazla iş var. Bunları toplu. Her şeyi bir kere planladık. Yayında birkaç saat sürdü tüm sürece.
Ve onları toplu bıraktık. Tüm gece boyunca çalışacağı şekilde. Avantajı ne oldu arkadaşlar? Size şöyle anlatayım. Belki bu normalde Claude Code dev ile belki 5 günüm 6 günüm alması gereken bir işti.
Onun yerine tüm planı baştan düzgün bir şekilde yaptığım için.
Düzgün bir sisteme soktuğum için. Her şey net olduğu için. Artık her şeyle bırakabildim modelleri.
Üstteki model sürekli alttaki agentları çalıştırıyor.
Ve EkoWerk'te bir tane sistem yaptım. Codex agentları çalıştırıyor. Benim serverıma yollayıp. Codex agentları serverdan PR açıyor. Bu PR'ı çekiyor. Bu sayede serverda da bir yandan iş yapılıyor.
Bir yandan burada yapılıyor. Her taraftan hızlıca iş yapmış oluyoruz. Codex agentlarının yapması gereken işleri yaparken.
Burada Claude agentlarının yapması gereken işleri yapıyor.
Gibi gibi. Ama bu da inanılmaz limitiyor. Yani şöyle diyeyim. Ben yaklaşık 2 gün önce limitlerimi resetledim.
2 günde şimdiden ben haftalık limitimin %90'ına geldim.
Claude Code 20x paketinde. Ama şöyle bir şey var. Bende bir tane daha 20x paket var. O da bu akşam yenilenecek. Oradan devam ediyor olacağım. Yani benim açımdan problem yok. Bilerek hızlı şekilde abanıyorum. Şurayı hızlı geçirmek için.
Bakın workflowlarımız bitti. 7 farklı bulgu çıkarttı. 7'sine doğruladı. Bunların çıkarttığı sonuçları kendi doğruladı.
Hepsi beklenen çıktığı verdi. Sonra hızlıca kontrolünü yapıyor. Kısaca bundan ibaret. Yani aslında Ultra Code'da bunu yapıyor. O zaman şimdi şeyi soracaksınız. Sen Claude'da nasıl Alt Agent olarak Codex'i çalıştırabiliyorsun?
Bu sorunun geleceğini tahmin ediyorum. Şimdi bakın arkadaşlar. Olay şu. Bilgisayarınızda Codex varsa ve Claude'da varsa.
İkisinde de giriş yaptıysanız. Yani bakın API'ye vesaire bulaşmıyoruz. API çok pahalı. İkisine de giriş yaptıysanız. Benim GitHub'da Codex üzerine bir tane skillim var.
I.SKills'dan bakabilirsiniz. Bu genel olarak modele Codex nasıl kullanacağını anlatıyor.
O kadar detaylı bir şey değil. Onu kullanarak model aslında. Siz nasıl Codex'e prompt atıyorsunuz.
Kendisi de Codex'e böyle prompt atıyor. Olay bundan ibaret aslında. Yani mesela diyorum ki atıyorum. Codex, exec ile.
Ki bunu demenize gerek yok. Codex at desenize yeterli. Hakındaysanız gene kendimi ifade ediyorum.
Agent orkestrasyonunda da aslında yapmanız gereken ilk bir şey yoktur arkadaşlar.
Sadece kendinizi modele ifade etmektir.
Yani yapay zekadaki çoğu şeyde olay bundan ibaret.
Kendinizi modele düzgünce ifade edin.
Yapmak istediğiniz işi model anlasın.
Model anladığı sürece eline de yeterli bilgi olduğu sürece zaten yapacak.
Herhangi bir problem yok. Problem şurada patlıyor. Onu da anlıyorum. Hangi soruyu soracağını bilmiyorsun ya. Bilmediğin sorunun ne olduğunu da bilmediğin için soramıyorsun.
Aslında modele sorsan model sana cevap verecek. Sorman gereken soruyu da bilmiyorsun. Bu tarz şeylerde kafanızda yaşadığınız problemi vesaire modeli anlatın.
Model ona göre plan yapsın. Yani her zaman orkestrasyon planı da kendiniz yapmayın.
Artık modellere olabildiğince fazla alan tanımaya bakın.
Alanı kısmak eskisi gibi değil.
Çok fazla limit vermeyin. Limiti bırakın model kendisi ayarlasın. Detayları kendisi ayarlasın. Siz genel olarak aklınızdaki planı anlatın.
Çekincelerinizi anlatın. Bakın şu olursa bana problem yaşatır. Bu olursa yaşatmaz gibisinden. Ona göre yapsın. Bakın hepsi cevabını verdim. Bu arada bu slide'ın da kopyası açıklamada var. Oradan kendinize bakabilirsiniz.
Hem Codex'te hem Claude Codeda yapabileceğiniz birkaç tane orkestrasyon sistemi gösteriyorum şimdi.
Mesela ilk başlangıç contextte ayırma.
Şu tarz promptla tık yollayarak yapabilirsiniz.
Şöyle bir sistem kuracaktır. Sen bununla konuşuyorsun. O alt agentleri yolluyor. Onlardan veri gelip sen geri geliyor. Mesela aynı mantık Codex'e attığımda da. Bakın Codex'e exec ile çalıştırma olabilir.
Deminki yaptığım gibi. Bunu nasıl yapabileceğinizi öğrenmiş olabilirsiniz. Bu sayede Codex'e de öyle çalıştırabilirsiniz.
Eğer direkt Codex'in uygulamasından yapıyorsanız buna ihtiyacınız yok.
Ancak kodeksi alt agent olarak çalıştıracaksanız bu işinize yarayabiliyor.
Şimdi Claude Codea tekrar dönüyorum. Atıyorum kendi alt agentini çalıştıracaksın.
İstersen böyle genel olarak agentın mantığı şu olsun diye bir kere bir standart hale getirebilirsin.
Ben değilim yapmayın gerek yok. Bakın gerek yok. Neden gerek yok dediğimde şöyle anlatayım size.
Zaten agent kendisi alt agentlara promptu veriyor.
Şu olabilir sürekli.
Sürekli belli şeyleri kullanıyorsunuz. Belli bir standart vardır. Bu olabilir. Bakın ciddiyemde olabilir. O standarta uymasını istiyorsundur agentlerin her zaman.
Ve sen baştan anlatmak istemiyorsundur.
O zaman Claude'a dersin ki sadece. Bana bu mantık çalışan bir agent lazım. Bak ne demiş. Sadece şunlara erişim olsun. Modeli bu olsun. Açıklaması bu olsun. Yani modelin görevi bu olsun. Ayarlar mısın deyin. Yapsın. Ondan sonra sürekli onu kullanır. Bunları yapabilirsin. Çekinmenize gerek yok. Ek olarak da Codex'e de alt agent yapmayı denetebilirsiniz.
Bunun bir seviyesi ne olur? Siz alt agentları böyle şuna ayır bunu ayır diye böyle vermeye başlarsınız.
Şu agent burada çalışsın. Bu agent şurada çalışsın gibisinden. Ondan sonra work trilleri anlamaya başlarsınız.
Work trillerle beraber dosyaları birbirinden ayırırsınız.
Ona göre agentler kendi alanında çalışırlar.
Test sistemlerine daha bloke etmeye başlarsınız.
Daha sistematik hale getirirsiniz. Daha sonra ne olur? Goallarla beraber çalıştırırsınız. Ve alt agentları da ona göre orkestre etmesini istersiniz.
Bunları yaparsınız. Şu şekilde yazmam lazım. Bu şekilde yazmam lazım. Gibi gitmek yerine. Sadece modelden istemeniz yeterlidir arkadaşlar.
Şey yapmayın. Bu kısmı da çok kasmayın. Ya ben mesela burada size mantığını anlatıyorum. Ama bunları kullanmanızda bu seviyede gerek yok.
Kesinlikle gerek yok. Ben de bu seviyede kullanmıyorum. Ben sadece arkada dönen mantığı anlatıyorum size.
Bir seviye daha dilleri yapınca. Workflowlarla biraz daha üst seviye atmanız gerekiyor.
Gerek var mı? Gene gerek yok. Çok gereksiz pahalı. Dediğim gibi sadece limitinizle alakalı olan durumlara göre bakarsınız.
Şey yapabilirsiniz mesela. Aynı görevi birden fazla agent yollarsınız.
O agentler aynı şeyi farklı farklı gözlerden incelerler.
Hata varsa mesela o hatayı çözebilirler.
Önemli kritik işlerde bunu yapabilirsiniz.
Peki niye diyeceksiniz? Niye böyle bir şey olsun ki diyeceksiniz? Arkadaşlar bakın bir model aynı görevi yazarken farklı düşünür.
İncelerken farklı düşünür. Aynı model aynı görevi. Tıp atıp aynı model şeyinde ve düşünce seviyesinde olsun.
İncelerken kendi yazdığı kodda hata bulabilir.
Buna şaşırmayın. Bazı durumlarda eğer önemliyse yapın. Daha da ileriye attıktan sonra artık belli kuralları verip.
Yani mesela sen bu gece boyunca çalışacaksın. Şu kurallara dikkat et. Şunları şunları yap. Alt içini çalışırken de bunlara dikkat et gibi.
Girip ondan sonra ise tüm gece çalışacağı şekilde bırakabilirsiniz.
Demin benim gösterdiğim gibi. Yani yaklaşık o dünkü yayından beri çalışmaya devam ediyor.
12 saat boyunca çalıştığım bir geceden notlarımı da aldım.
Kendi notlarıma baktım. O gece neler olmuş? Yani çünkü birçok şey patlıyor arkadaşlar. Mesela jev gecesi. Jev'i kurduğumuz gece. Birçok şey patlıyor. Onları çözüyoruz. Başka bir şey patlıyor. Başka bir şey çözüyoruz. Ama zamanla oturuyor. Bakın görüyor musunuz? Bazen redler oluyor. Bazen problemler oluyor.
Ama genel olarak orkestrasyon mantığını başta oturttuğumuz için.
Her şey istediğimiz yere yavaş yavaş varıyor.
Bir yerde patlıyor. 87 dakika boyunca internet olmuyor. Ondan sonra o da düzeliyor. O da düzelince her şeyi çözmüş oluyoruz.
İşin sonundaysa. Bakın tüm agentların yaptığı iş tek bir yerde artık birikmiş oluyor.
Ve tüm iş artık bizim kendi code base'imizde olmuş oluyor.
Toplam 48 tane agent olmuş. 13 farklı PR çıkartmışız işin sonunda.
Ve bunların hepsini artık geçirmişiz main'e.
Şimdi eğlencesine beraber bir orkestra kuracağız.
Bakın böyle bir sistem var. Tamam mı? Farklı farklı işler için. Nasıl sistemler yapman gerektiğine dair?
Demiş ki mesela videografi yapacaksın.
Nasıl bir altı ecen sistemi kuracaksın? Örneğin bir tane daha Astra eklemek ister misin?
Bir tane daha Luna eklemek ister misin? Gibi gibi. Ben direkt önerilerini kur diyorum.
Çal diyorum. Neden astralar var? Çünkü zaten bu videografi işi. Görsel işlerine falan çok daha iyi çalıştığı için. Genel olarak onu kullanıyorum. Biliyorsunuz. Atıyorum mesela hata düzeltme işi. Gene önerilerini kur diyorum. Bak ne yaptı mesela? Astra ve Opuslar ile beraber kurdu bu sefer.
Genel olarak bizim limitlerimiz yüksekken.
Tabii ki daha bu tarz modelleri tercih ediyoruz.
Her zaman değil. Araştırma rapor dedim. Bakın önerilenleri kur dedim. Neden bu sefer çok fazla Luna kullandık biliyor musunuz?
Çünkü Luna bu logları tek tek okuyacak.
Hızlı hızlı temizleyecek. Benzer şeyleri birbirinden ayıracak vs.
Ondan sonra Opuslara vs. verecek. Olay bundan ibaret. Bu sayede daha az token harcayıp daha kısa sürede daha az problemli hepsini çözebileceğiz.
Ben Luna'yı kendi kullanımda sadece bu işi için kullanıyorum şu an.
Şimdi bakın her zaman işe yaramaz bu orkestra işi.
Her zaman gerek yoktur. Her zaman kullanmanıza gerek yoktur.
Çünkü her iş paralel değil.
Her iş paralel değil. Mesela kendim demişim. Bak bunda paralel agent kullanmayalım sırayla komit komit gidelim.
Çünkü her iş paralel değildir arkadaşlar. Bakın mesela bir yerde belli şeyler takılmış. Codex kendi kendine tüm kontrolü eline aldı.
Dedi ki bu takılıp duruyor. Burada gereksiz limit yakıyoruz. Bir yere de varamıyoruz. Tak diye iptal etti. Yani bunları da zaten artık agentler yapabiliyorlar.
Veya atıyorum mesela demişim ki bakın artık bu kadar agresif gitme.
Limitimiz o kadar yüksek değil artık. Buna dikkat ederek daha fazla şey yapmışım. Veya atıyorum ön beylek şişmiş. Onları ayrı bir şekilde yapmışım. Vesaire vesaire. Her zaman alt agent'a gerek yok. Çünkü alt agent loglarını da tutuyor. Şeylerini de tutuyor. İşlerin kaydını tuttuğu için zamanla birikmeye başlayabiliyor.
Genel olarak bazı aldığımız kararları göstermiş.
8 farklı kararı derlemiş. MacOS'ta timeout olmaması üzerine bir tane hata yaşamışız.
Ben bilgisayarına saçmamış şekilde 3 farklı Codex sürümü kurmuşum.
Burada bir problem yaşamışız. 3'ü de aynı bilgisayarda olduğu için agent hangisini çalıştıracağına emin olamıyordu.
Onları çözdük. Git kullanım ile alakalı ağustos'ta bir problem yaşadım küçük.
Genel olarak zaten problemler bu tarz şeylerde git kullanım ile alakalı olabiliyor.
Eğer agent problem yaparsa. Bakın mesela yapmış burada ne yapmış. Git resetlemiş. Oradaki başka bir oturumun komitlenmemiş yarıda kalan işi silindi.
Bak oturumun işi silindi. Artık çok çok çok nadiren yaşıyorum bunları.
Ancak olabiliyor. İmkansız değil. Hata yaptı. Çünkü kendi yaptığı hatayı düzeltmeye çalışırken farklı bir hata yaptı.
Geçici testleri nereye koyacağı vesaire üzerine küçük hatalar olmuştu.
Onları çok takmayın. Ona önemli değil.
Kalanlarda o kadar problem değil aslında.
Yani genel olarak arkadaşlar mantık tamamen budur.
Bakın agent orkestrasyonu yaparken.
Tek gereken şey. Tek gereken. Bakın özetliyorum tamamen. Bu işi ben bir orkestra yönetiyor olsam nasıl yönetirdim?
Bakın bir şef olsam nasıl yönetirdim?
Nasıl yönetirdim? Düşünelim. Nasıl yönetirdiniz? Geniş bir iş yapacağım. Benim bu işi yapmam için alttakilerin de.
Mesela çünkü alttakiler sıfırdan başlıyor değil mi?
Bir an doğuyorlar. O anlık doğuyorlar. Alt agentler eskidekisinin verinize sahip değil.
O an doğuyor. Ama bu işi doğru yapması için eski bilgimi bir yerden alması lazım.
Ama hepsini alırsa o zaman da benim alt agent kullanmamın mantığı yok.
Çok fazla token yer. Çok fazla problem olur. Ne o zaman kilit bilginin alması lazım. Bu kilit bilgiyi ben nasıl buna veririm?
Ben üstteki agentla konuşurum. Üstteki agentla derdimi anlatırım. Üstteki agent ona göre hepsinin ortak çalışabileceği bir protokol kurar.
O protokolü üstteki agent tasarlar. Bakın çözdük problemi. Peki benim elimde belli miktar Claude limiti var.
Belli miktar Codex limiti var. Ben bu ikisini kullanmak istiyorum. Havada kalsın istemiyorum. Ne yaparım? Ona göre derim ki benim elimde bu kadar Claude, bu kadar Codex limiti var.
İşlerin bir kısmı Codex'e gömelim. İşlerin bir kısmı Claude'a gömelim. Codex agentları şu şu şu işler değildir.
Detaylı promptlar yazdığında onu çok iyi yapar.
Ona göre ona davran. Claude agentları da çok detay sevmez. Kendi başına buyruktur. Biraz daha onu alan tanı. En son yaptığı işi bir kontrol et. Bakın. Gene aynı mantık. Onun dışında bazı işler kolay. Kolay işlere sen Sonneti yolla. Gerek yok. O pusuza gerek yok. Bunu diyebiliriz mesela. Ve atıyorum sen lunayı yolla büyük veriyi temizlemek için.
Bunu diyebiliriz. Bunları dediğimizde bunların her birini bir protokol yerine getirdiğimizde zaten.
Bir kere yaptıktan sonra bir daha bir şey yapmamıza gerek yok.
Özel bir uygulama almanıza gerek yok. Özel bir sistem kurmanıza gerek yok. Zamanla kendi ihtiyaçlarınıza göre bunu değiştirebilirsiniz zaten.
Bunu yaptığımızda arkadaşlar. Bildiğiniz bir orkestra yönetiyor olacağız.
Ciddi anlamda kaliteli bir şekilde çalışan.
Her şeyin düzgün çalıştığı. Ve kendi yaptığımız işten memnun olacağımız.
Ve işimizi hızlandıracağımız bir sistem kuruyor olacağız.
Arkadaşlar bakın bunun kaçar yolu yok.
Kulağa biraz zor ve karmaşık geliyor. Farkındayım. Ancak ben genel olarak size hem işin karmaşık kısmını hem kolay kısmını anlatmaya çalıştım.
Bunda nedeni şu. İşin karmaşık kısmına girmenize gerek yok.
Ciddi anda gerek yok. İşin karmaşık kısmını bir kere şu videoyu izlediğinizde teorik bilgiyi alın bitti.
Gerek yok. Unutun. O an sadece arkadaki mantığı kafanızda oturun. Sadece önemli olan nokta şu. Genel olarak bir orkestrasyon yapmadan önce olaya yapay zekanın penceresinden bakın.
Yapay zeka veriye erişemezse problem yaşar.
Yapay zeka diğer agentler ne iş yapıyor onu takip edemezse problem yaşar.
Yapay zekada mesela bir agent yer agentin yaptığı işe bulaşıyorsa problem çıkar.
Bunların hepsi birer basit örnek. Bunları kafaya oturttuktan sonra zaten agent'a ona göre yaklaşmaya başlıyorsun.
Ona göre orkestrasyon yapıyorsun. Peki orkestrasyon yapmak zorunda mıyız? Ya biraz zorundayız artık. Neden zorundayız? Çünkü artık herkes agent yönetiyor değil mi?
Ne oluyor? Artık işi bizim hızlandırmamız ve kaliteyi çok arttırmamız lazım.
Bakın hem hızlandırma hem kaliteyi çok arttırma. Örneğin ben mesela tek bir acıt da baştan sona sürekli feedback yapa yapa üzerinde uğraşı uğraşı.
Şu slide'ı yapmaya kalksam arkadaşlar o kadar görsel o kadar animasyon o kadar video şu bu filan derken her biri derken üstüne bile bunlara da kalmıyor.
Benim bloglarımdan çıkan veriler vesaire bunların her birinin nedenli zaman alacağını düşünün.
Her bir görsel üretilecek. Her bir video üretilecek. Bloglarım toplanacak. Bloglara göre biz böyle simülasyonlar yapacağız.
Biz bunları yaptıktan sonra bunları belli bir sunum haline getireceğiz.
Animasyonlarını yapacağız. Ondan sonra onları birleştireceğiz. Bir hikaye haline getireceğiz. Onları da yaptık. Bunu belli bir sıraya alacağız. Bak ne yaptım ben mesela size terminalde belli prompt örnekleri ve onun sonuçlarını gösterdim.
Bunları hazırlayacağız. Arkada çalışan promptlara vesaire. Yani arkadaki işin büyüklüğünü düşünün bir.
Bir kafa yorun. Şurada yapılan her ayrıntıya bir dikkat edin.
Bu yapılabilecek bir iş değil. Bu insani bir iş değil. Ben manuel olarak tek bir agent da bunu yapmaya kalksam çok zamanım alır.
Gerçekten çok zamanım alır. Yetiştiremezdim değil mi? Ben ama nasıl hem kanala yetişiyorum. Hem bu videoyu editleyeceğim atacağım. Hem küçük resimlerini yapıyorum. Açıklamasını şunu bunu. Yorumlarınıza cevap veriyorum. Kendim serayıya kod yazıyorum. Bunların hepsini nasıl yapıyorum sizce aynı anda?
Başka türlü mümkün olabilir mi? O yüzden mecburen orkestrasyonu öğrenmeniz zamanla gerekecek.
Çok kafaya takmayın ama mantığını anlayın.
Paralel agentları kullanın. Tek bir agent da kalmayın. Genel olarak diyeceklerim bu kadardı. Daha önce zaten belli videolarımda Paralel agent kullanma örnekleri, benim nasıl kullandım vesaire bunlara değindim.
Her şeyi genel del toplu toplamaya çalıştım. Burada eğer kapınız karışan konular varsa o videolara da bakabilirsiniz.
Bu Yapay Zekay Sıfırdan Başlama serisinin bir sonraki videosuydu.
Uzun bir video oldu. Önceki videoları da izlemediyseniz onlara da bakabilirsiniz.
Umarım videoyu beğenmişsinizdir. Fikir ve düşüncelerinizi yorumlarda paylaşmayı unutmayın.
Bir sonraki videoya kadar hoşçakalın. Altyazı M.K.
