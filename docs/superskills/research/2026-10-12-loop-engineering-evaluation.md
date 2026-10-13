# Loop engineering: kaynak araştırması ve iki ortamda değerlendirme — 2026-10-12

## Sonuç ve önceki kapanışın düzeltmesi

İlk ekleme için yapılan statik kontroller, canlı davranış doğrulaması değildi. Önceki kapanış bu ayrımı yeterince güçlü ifade etmedi. Bu çalışma; birincil kaynakları, uygulama kodunu, iki güncel konuşmanın transkriptini ve gerçek Codex/Claude çalıştırmalarını ekler. “En başarılı entegrasyon” veya yüzde verim artışı iddiası hedeflenmez: bu iddialar temsili işler ve tekrarlı ölçüm gerektirir.

Sonuç: iki ortamda da üç sürümün yedi vakalık **dış sonuç kontrolü** 7/7. Eski sürüme göre tamamlanma/bütçe sonuçlarında üstünlük gösterilmedi. Trace incelemesi protokol ayrıntılarının skorun dışında kaldığını da gösterdi; dolayısıyla 7/7 tam talimat uyumu veya genel güvenilirlik oranı değildir.

## Kavramın kapsamı ve bizim karşılığı

[LangChain’in dört döngü ayrımı](https://www.langchain.com/blog/the-art-of-loop-engineering) faydalı bir çerçeve; tek evrensel standart değildir. İç yürütme → doğrulama → tekrar tetiklenme → izlerden sistem iyileştirme katmanlarını birbirine karıştırmamalıyız.

| Katman | Bu kütüphanedeki karşılık | Sınır |
|---|---|---|
| Araçlarla yürütme | Host agent döngüsü + mevcut `executing-plans` | Skill yeni agent runtime yaratmaz. |
| Sonuçtan geri besleme | Koşullu `loop-control.md`: kriter, kanıt, bütçe, durma ve resume | Sert süre sınırı runtime'da; talimata uyum ayrıca değerlendirilir. |
| Tekrar/event tetiklemesi | Referansta koşullu runtime sözleşmesi | Scheduler kurulmadı; tetikleyici, run kimliği ve overlap desteği host'a ait. |
| İzlerden iyileştirme | Referanstaki ayrı adımlar: teşhis → eval vakası → aday → eski/yeni karşılaştırma | Çalışan agent kendiliğinden kriterlerini veya skill'ini değiştirmez. Yeni servis/ürün zorunlu tutulmadı. |

Böylece kavramın tüm katmanları için yer ve sınır belli; yalnız yürütme davranışının aşağıdaki küçük alt kümesi canlı test edilmiştir.

## Birincil kaynaklar: ne okundu, ne alınmadı?

Erişim tarihi 2026-10-12. “Güncel” ifadesi kontrol edilen sürüme ilişkindir; eski ama hâlâ ilgili birincil yazılar da ayrıca tarihlendi.

| Kaynak | Tarih | Alınan ilke / sınır |
|---|---|---|
| [Addy Osmani, Loop Engineering](https://addyosmani.com/blog/loop-engineering/) | 2026-06-07 | İlerlemeyi görünür kontrol sonucuyla yöneltme; scheduler/delegation her görev için şart sayılmadı. |
| [Sydney Runkle, The Art of Loop Engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) | 2026-06-16 | Dört döngü; doğrulamanın da süre ve kaynak maliyeti var. Her işte daha çok tekrar verimli olmayabilir. |
| [Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | 2026-01-09 | Son yanıt yerine sonuç durumu; dış grader, kontrol örnekleri, izolasyon ve trace incelemesi. Yedi sentetik vaka temsili performans benchmark'ı sayılmadı. |
| [Anthropic, Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 2025-11-26 | Kalıcı ilerleme ve yeniden doğrulama; demo otomatik commit yaklaşımı alınmadı. |
| [Anthropic, Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents) | 2026-04-08 | Bağlamdan ayrı kalıcı durum; managed ürün özellikleri Markdown'ın özelliği gibi sunulmadı. |
| [LoopArena ön baskısı](https://arxiv.org/html/2608.28281v1) | 2026-08-28 | Sabit görev, kanıt paketi ve kontrollü karşılaştırma. Makalenin controller/worker benchmark sonuçları bizim skill kazanımımız değildir. |
| [Loop Engineering: Building Blocks, Adoption, and Impact ön baskısı](https://arxiv.org/html/2608.21884v1) | 2026-08-22 | Repo'da kural bulunması runtime'da uygulanmasıyla aynı şey değil. Çalışmanın planlanan kontrollü deneyleri olmuş sonuç sayılmadı. |

Ön baskılar hakemli performans garantisi değildir. [Loopcraft](https://www.latent.space/p/loopcraft), 2026-06-12, terminoloji bağlamı için okundu; uygulama kuralları için yukarıdaki birincil kod/dokümanlara ağırlık verildi.

## GitHub incelemesi: sürümler sabitlendi

Aşağıdaki commit'ler API ile tespit edildi, dosyalar bu SHA'larla indirildi. Tam repo testi çalıştırıldığı veya bütün dosyaların okunduğu iddia edilmiyor.

| Repo / sabit sürüm | İncelenen dosyalar ve bulgu | Taklit edilmeyen davranış |
|---|---|---|
| [Claude quickstarts](https://github.com/anthropics/claude-quickstarts/tree/9ec32b91df50b0d4906cae64b13c6298055ff40d/autonomous-coding), commit 2026-10-07 | `agent.py`, `progress.py`, coding prompt ve kurulum dosyaları. İlerleme dosyası ve görev bazlı kontrol faydalı. | İterasyon sayacı süreç başında sıfırlanıyor; sınırsız mod ve agent'ın yazdığı pass bayrağı tek başına kesin tamamlanma kanıtı değil. |
| [Deep Agents](https://github.com/langchain-ai/deepagents/tree/4bb4c7fcbf5f2ef65c39ea0134c42555926bd40b), commit 2026-10-11 | Rubric örneği bütünüyle; middleware ve testlerin kriter sayımı, freeze, eksik grade, `grader_error`, sınır/resume bölümleri. | İlk kriter ayrıştırmasının eksiksizliği garantili sayılmadı; ürünün yeni grading run için sayaç yenilemesi bizim “aynı işi resume” kuralımıza taşınmadı. `goal_rubric.py` indirildi ama bütünüyle incelenmiş sayılmadı. |
| [Autoresearch](https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117), commit 2026-03-26 | `program.md` ve README: sabit değerlendirme, baseline, sonuç kaydı, değişikliği kabul/reddetme. | Sonsuz döngü ve otomatik git commit/reset; kullanıcı/repo sınırlarıyla uyumsuz. Model eğitim metriği skill verimine genellenmedi. |
| [LoopArena](https://github.com/AMAP-ML/LoopArena/tree/0a939224a15c4ebc895ad25d71a398fbb9513fd6), commit 2026-09-08 | README, sabit controller ve controller sözleşme kontrolleri. | Sabit controller'ın worker'ın “done” beyanına dayanması, kanıta uyarlanan denetleyici örneği sayılmadı. |

Yerel kaynak snapshot'ı: `/var/folders/j1/c3cj_b612tbdyjtdgrhnk2zr0000gn/T/loop-research-td5xbgjr`. Dış ağaçlar kurulu skill dizinlerine taşınmadı.

## Son bir ayda uzman konuşmaları ve transkriptler

Konuşmaların etkinliği [LangChain'in resmi NYC sayfasında](https://interrupt.langchain.com/nyc) 2026-09-24 olarak doğrulandı: 2026-09-12–2026-10-12 penceresinin içinde. Video bağlantıları [resmi kayıt listesinden](https://interrupt.langchain.com/interrupt-recordings) kontrol edildi. Yükleme gününü etkinlik günüyle karıştırmıyoruz; keynote için ikincil sonuçlarda 2026-10-05 görülse de asıl güncel olma kanıtı resmi etkinlik tarihidir.

| Konuşmacı ve birincil video | Okunan bölümler | Yerel transkript |
|---|---|---|
| [Harrison Chase — NYC Opening Keynote](https://www.youtube.com/watch?v=950byF7njfw), LangChain kurucu ortağı/CEO | 05:57–06:48 hata/kalite; 08:46–09:17 yaşam döngüsü; 19:45–21:03 trace; 26:03–28:46 doğrulanmış düzeltme | [Keynote transkripti](/Users/alparslankiilinc/Desktop/transkript/output/Interrupt%20NYC%20Opening%20Keynote.md) |
| [Ben Tannyhill — Building Engine v2](https://www.youtube.com/watch?v=S3l7U7gOsyY), Engine ürün yöneticisi | Tam 00:05–20:02 metin; özellikle 02:11–06:37 ayrı görev eval'leri/gerçek kullanım; 10:26–12:55 izler arası fark; 13:30–15:50 eski/yeni replay + regresyon; 18:04–19:31 model değişimini önce ölçme | [Engine v2 transkripti](/Users/alparslankiilinc/Desktop/transkript/output/Building%20Engine%20v2%20How%20LangChain%20approaches%20agent%20improvement.md) |

İkisi de kullanıcının `yt-captions-md --lang tr,en --timestamps` aracıyla başarıyla çıkarıldı. Otomatik altyazıdaki sözcük hataları nedeniyle birebir alıntı yerine zaman damgalı çıkarımlar kullanıldı. Ürün tanıtımı ve şirket içi sonuçlar bizim ölçümümüz sayılmadı; yöntem alındı. Eski Temmuz videosu “son bir ay” örneğine dahil edilmedi.

## Bu turdaki her değişikliğin gerekçesi

İlk eklemenin dosya bazlı gerekçeleri [önceki raporda](2026-10-12-loop-control.md). Bu turdaki farklar:

| Değişiklik | Gerekçe / dayanak | Doğrulama sınırı |
|---|---|---|
| `loop-control.md`: kriterleri sabit tutma, kriter başına kontrol, deterministik kontrol veya açık rubric | Deep Agents'taki eksik kriter/grade kontrolleri ve Anthropic eval yaklaşımı. Başarı hedefi deneme sırasında küçülmesin. | Calculator vakası yalnız deterministik kontrolü sınar; model grader sınanmadı. |
| Bütçe birimi; başlayan başarısız deneme ile hiç çalışmayan komutu ayırma | İlk Claude izlerinde birleşik shell çağrıları reddedildi. “Her deneme” belirsizliği yerine supplied unit korunur; zaman yine tüketilir. | Bütçe fixture'ları action+check birimini kullanır; token limiti uygulanmadı. |
| Pending action kaydı ve resume'da yan etkiyi uzlaştırma | Kalıcı durum yaklaşımı; kesintide tamamlanıp kaydedilemeyen işlemi iki kez uygulama riskini açıklığa kavuşturur. | Gerçek süreç çökmesi/enforced idempotency testi yapılmadı; tasarım ilkesi. |
| Check altyapı hatasını davranış hatasından ayırma | Deep Agents `grader_error`; bu çalışmadaki cache/grader hatası ve kullanım limiti somut karşı örnekler. | Canlı quota hatası görüldü; bozuk model grader ayrı canlı vaka olarak sınanmadı. |
| Koşullu recurring run sözleşmesi | Dört döngü çerçevesindeki tetikleme katmanının sahibini belirtir. Host/run ID/overlap/bütçe olmadan otomasyon varmış gibi konuşulmasın. | Scheduler kurulmadı veya test edilmedi; kullanıcının mevcut isteği skill metniyle ilgili. |
| Ayrı trace→eval→aday→karşılaştırma adımları; mevcut uzmanlara yönlendirme | Ben'in tekrar üretme ve aynı girdilerde eski/yeni doğrulama yöntemi; mevcut `diagnosing-workflow`/`writing-skills` sorumluluklarını yeniden kullanır. | İşleyen agent'ın kendini kontrolsüz değiştirmesi değil; bu turda yöntem uygulandı. |
| `tests/loop_agent_eval.py` | Kullanıcı gerçek değerlendirme istedi. Temiz fixture, sabit skill kopyası, gerçek CLI, dış sonuç kontrolü ve yerel trace üretir. | Testler açıkça skill seçer; otomatik routing veya tam uygulama benchmark'ı değildir. |
| Grader iyi/kötü/integrity/partial-coverage/yan etki kontrolleri ve salt-okunur dış grade | İlk kontrolün cache sorunu ve trace okumada bulunan eksik koruma, test aracının da doğrulanması gerektiğini gösterdi. | Davranış regresyon grader'ı; düşmanca agent'a karşı güvenlik sandbox'ı iddiası yok. |
| Selective infrastructure retry, limit sonrası yeni işleri durdurma ve timeout cleanup | Kullanım limiti nedeniyle aynı ortamda körlemesine çağrı devam etmesini engeller; biten sonuçları korur. | Hâlihazırda başlayan paralel bir çağrı da limit hatası alabilir. Sessiz ücretli API fallback yok. |
| `tests/run-all.sh`: yalnız `--self-test` | Yeni grader'ın bozulması standart gate'te yakalansın; default test model/kota tüketmesin. | Canlı başarı statik gate'ten çıkarılmaz. |
| `tests/README.md`, manual cases, docs indeksi ve bu rapor | Komut, kaynak, gerçek sonuç ve test edilmemiş durumları bulunabilir kılar. | İlk rapor tarihsel kayıt olarak korunur. |

`executing-plans/SKILL.md` bu ikinci turda değişmedi; açıklama/routing cue'ları ve 16 v1 skill sayısı korunuyor. Ayrıntı koşullu referansta. Ref 576 → 990 whitespace kelime oldu; bu ilaveyi bir verim kazanımı gibi sunmuyoruz. Ana skill normal işte yeni hazırlık istemiyor; referansın kendisinin fazladan yüklenmesi bu grader'ın otomatik assertion'ı değil.

## Değerlendirme protokolü

Üç sürüm: **baseline** = loop öncesi executing-plans; **v1** = ilk küçük ekleme; **v2** = bu turdaki referans. Diğer skill dosyaları aynı sadeleştirilmiş kopyadan. Her hücre bir gerçek agent çalıştırması; modeller arası toplam tek oran yapılmaz.

- Codex CLI `0.162.0-alpha.17.2`, `gpt-6-astra`, medium effort, standard, workspace-write.
- Claude Code `2.1.291`, event'te raporlanan `claude-opus-5-5`; restricted, acceptEdits, prompts none, Read/Write/Edit ve standalone python3; MCP/slash session ayarları kapalı.
- Geçici ayrı çalışma alanları; kullanıcı ayarları kapalı; AGENTS ve plan açık; host policy bypass yok. Gerçek mevcut CLI hesapları kullanıldı.
- Her süreçte 240 saniye wall timeout; en fazla 10 saniye terminate grace ardından zorla kapatma. İterasyon sayısı task sözleşmesinde; dış grader gözlemleyip değerlendirir, fiziksel tool cap yok.
- Plan/skill snapshot SHA-256 manifest'i, JSONL CLI events, final yanıt, ledger ve sonuç dosyaları tutulur. CLI bayraklarının tam hali [test aracında](../../../tests/loop_agent_eval.py).
- Yedi vaka: sıradan label değişikliği; ikinci turda başarı; iki tur budget; resume'da kalan tek tur; ilerlemeyen cihaz; stale “done” kaydı; targeted pass'in yetersiz olduğu iki kriterli calculator.
- Kriterler modelin son yanıtına göre değil fixture'ın dış sonucu, çalıştırma sayısı, kontrol kapsamı ve korunması gereken dosyalara göre puanlandı. Son durum dilinin nüansı ayrıca loglardan okundu; regex tek başına güçlü semantik grader değildir.

## Protokolde bulunan hatalar ve müdahaleler

1. İlk offline grader kontrolü calculator import cache'i yüzünden başarısız oldu. Başarısız kontrol sonrasında yanlışlıkla başlatılan pilot durduruldu; o pilot kalite sonucuna katılmadı. Güncel grader mevcut kaynağı compile eder; import cache kullanmaz.
2. İlk matrisin son dokuz Codex denemesi kullanım limitine takıldı. Bu kayıtlar altyapı hatasıdır; skill başarısızlığı değildir. Kullanıcı “devam, limit bitmişti” dedikten sonra yalnız bu dokuz hücre aynı frozen skill dosyalarıyla yeni fixture'da tekrarlandı. İlk kayıtlar silinmedi.
3. Trace incelemesinde calculator görevlerinde ilgisiz `action.py` çağrıları görüldü. Önceki grader `artifact.json` yan etkisini korumuyordu; fixture'ın komut cümlesi de her iki helper'ın çalıştırılması istenmiş gibi okunabiliyordu. Koruma eklendi ve cümle açıklığa kavuşturuldu. Stale/partial vakaları **üç sürüm × iki ortamda** tekrarlandı; önceki calculator skorları son tabloya taşınmadı. Bu düzeltme skill metninin üstünlüğüne kanıt sayılmadı.
4. Dış grader başlangıçta verifier çağırarak agent trace'ine fazladan check ekliyordu. Dış grade salt-okunur hale getirildi. İlk sonuçtaki `agent_checks` sayısı grade öncesi yakalanmıştı; yine de mevcut sürüm tekrar grade'in izleri değiştirmemesini kontrol eder.

## Canlı sonuçlar

42 seçilmiş hücre: 7 vaka × 3 sürüm × 2 ortam. Her hücre n=1. Calculator hücreleri düzeltilmiş follow-up'tan; quota nedeniyle kesilen hücreler açık kullanıcı devam isteği sonrası tekrarından alınır. Başarısız ilk kayıtlar arşivde korunur.

| Ortam | Sürüm | Dış sonuç kontrolü | Medyan süre, sn |
|---|---|---|---|
| codex | baseline | 7/7 | 47.97 |
| codex | v1 | 7/7 | 47.86 |
| codex | v2 | 7/7 | 54.22 |
| claude | baseline | 7/7 | 37.25 |
| claude | v1 | 7/7 | 36.62 |
| claude | v2 | 7/7 | 46.59 |

V2 medyanı her iki ortamda da bu örneklemde daha yüksek çıktı; daha hızlı çalıştığı gösterilmedi. Bu ek talimatların maliyetini gizlemiyoruz. Medyanlar yalnız bu çalıştırmaların betimlemesi; genel hız veya yüzde verim kazancı tahmini değil. Kota kesintisi sonrası tekrarların zaman aralığı farklı; sıra, cache, hesap yükü ve tek tekrar ölçümü etkiler. Token alanları [JSON sonuçlarda](loop-eval-2026-10-12/results.json) ham platform semantiğiyle saklandı; Codex'in cached input alanlarıyla Claude'un ayrı cache read/write alanları tek bir maliyet oranına birleştirilmedi.

Gözlenen davranışlar:

- Bütün sürümler istenen action bütçesinde durdu; stale ve partial hücrelerinde güncel tam kontrol çalıştı. Korunan iş ve frozen skill dosyaları seçilmiş 42 hücrede aynı kaldı.
- Baseline bütçe durmasını `blocked`, v1/v2 `budget-exhausted` diye raporladı: status ayrımı görünür oldu, daha çok işi tamamladığını göstermiyor.
- Claude stalled vakasında baseline iki, v1 bir, v2 bir action çalıştırdı; Codex hepsinde bir. Bu tek gözlem tekrar israfının genel olarak azaldığını kanıtlamaz.
- Claude baseline second-pass ledger'ı, ilk kaydın ikinci action ile aynı tool batch'te yazıldığını ve sıra garantisinin olmadığını bizzat kaydetti. Dış grader bu checkpoint sırasını puanlamıyor. V2 pending-entry tasarımı var, fakat gerçek crash recovery veya her action'dan önce durable checkpoint doğruluğu 7/7 skoruyla kanıtlanmış sayılmıyor.
- Claude bazı okuma/compound shell komutlarını permission nedeniyle yeniden denedi; bu sürümlerin tümünde görüldü. Codex/Claude farkı yalnız skill metnine bağlanamaz.

Bu set şu an **regresyon taraması**: baseline zaten bütün dış sonuçları geçiyor. Genel başarı artışını gösterecek bir capability benchmark'ı olarak doygun. Sonuçların eşit çıkması yeni kuralları başarılı optimizasyon saymak için gerekçe değil. V2, yukarıdaki belirsizlikleri ve kaynaklarla desteklenen sınırları açıklığa kavuşturduğu için tutuldu; bu, ölçülmüş kalite/verim üstünlüğünden ayrı gerekçedir.

## Yerel kayıtlar ve tekrar çalıştırma

Ham kayıtlar şu dizinlerde; paylaşılmadı:

- `/tmp/superskills-loop-round1-fixed`: baseline/v1, ilk 28 hücre.
- `/tmp/superskills-loop-round2-v2`: v2, ilk 14 hücre.
- `/tmp/superskills-loop-round1-retry`, `/tmp/superskills-loop-round2-retry`: quota nedeniyle kesilen dokuz deneme.
- `/tmp/superskills-loop-calculator-followup`: düzeltilmiş iki calculator vakası, bütün sürümler/ortamlar.

Bunlar geçici dosyalardır. Kalıcı kayıtlar: [sonuçlar ve 63 kayıtlı deneme](loop-eval-2026-10-12/results.json), [snapshot/harness SHA manifest'leri](loop-eval-2026-10-12/manifests.json), [seçilmiş 42 son yanıt](loop-eval-2026-10-12/selected-responses.md), [karşılaştırılan executor metinleri](loop-eval-2026-10-12/instructions/baseline/executing-plans/SKILL.md). Bu 63 kayıtta dokuz quota hatası, 12 yeniden değerlendirilen eski calculator sonucu ve 42 seçilmiş hücre var. İlk smoke/iptal edilen pilotlar bu sayıya dahil değil. Özel session ID ve ham CLI JSONL repo'ya konmadı.

```bash
PYTHONDONTWRITEBYTECODE=1 ./tests/run-all.sh
python3 tests/loop_agent_eval.py --out /tmp/loop-new-screen --variants current --platforms codex,claude
# Yalnız altyapı nedeniyle kesilen işleri, kaynak skill snapshot'larıyla yeniden dene:
python3 tests/loop_agent_eval.py --out /tmp/loop-retry --retry-from /tmp/loop-new-screen --platforms codex,claude
```

## Ne kanıtlamıyor?

Tek trial/hücre, yedi sentetik ve görev talimatı açık fixture: başarı oranındaki küçük farkları ya da günlük verimi güvenilir tahmin etmez. Canlı otomatik skill seçimi, scheduler, crash recovery, gerçek uzun context compaction, çoklu grader kararı ve kullanıcının gerçek uygulama işlerinde A/B denenmedi. Bu alanlarda “entegre edildi ve en iyi sonuç verdi” denmez. Gelişmeyi ölçmek için gerçek başarısız işlerden ayrı bir veri seti ve birden fazla tekrar gerekir; sırf daha yüksek skor almak için hedef/başarı tanımı değiştirilmez.

## Son doğrulama

`PYTHONDONTWRITEBYTECODE=1 ./tests/run-all.sh`: exit 0 — 16 skill, 32 TR + 49 EN trigger, 81 benzersiz TR token, 26 router hedefi, 13 optional, 6 sentetik routing senaryosu; offline loop grader kontrolleri geçti. `git diff --check`: exit 0. Bunlar canlı kalite skorundan ayrı gate'lerdir. Sonuç arşivi, snapshot'lar ve yerel belge bağlantıları ayrıca kontrol edildi. Commit/push/kurulum yapılmadı. Kullanıcının önceden değişmiş kök README dosyası snapshot ile byte-for-byte aynı kaldı.
