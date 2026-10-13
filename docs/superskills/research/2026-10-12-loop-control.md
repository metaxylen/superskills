# Loop kontrolü eklemesi — 2026-10-12

Bu dosya ilk, yalnız statik kontrol yapılan eklemenin tarihsel kaydıdır. Sonraki kaynak/kod/transkript araştırması, metin düzeltmeleri ve iki ortamda canlı değerlendirme [ayrı raporda](2026-10-12-loop-engineering-evaluation.md). Aşağıdaki “çalıştırılmadı” ifadeleri ilk aşamanın durumunu anlatır.

## Kapsam

Kullanıcının loop engineering ekleme isteği, mevcut `executing-plans` skill'ine koşullu bir referansla uygulandı. Yeni skill, routing açıklaması, otomatik scheduler veya agent filosu eklenmedi. Sıradan plan görevleri mevcut adımları kullanır.

## Kaynaklar ve sınırları

Kaynaklar 2026-10-12 tarihinde yeniden web üzerinden okundu. Makalelerin yayın tarihleri erişim tarihinden farklıdır.

| Kimlik | Birincil kaynak | Alınan ilke ve sınır |
|---|---|---|
| S1 | [Addy Osmani: Loop Engineering](https://addyosmani.com/blog/loop-engineering/), 2026-06-07 | İş seçimi, yürütme, kontrol ve kalıcı durumun birlikte tasarlanması. Yazıdaki scheduler, connector ve subagent seçenekleri her görev için zorunlu parça sayılmadı. |
| S2 | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), 2024-12-19 | Gerçek araç sonuçlarıyla ilerleme, durma koşulları ve en basit yeterli yapı. Sayfanın eski araç bilgileri için güncel Managed Agents yazısına yönlendirmesi takip edildi; eski ürün/bayrak bilgisi kopyalanmadı. |
| S3 | [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), 2025-11-26 | Oturumlar arasında ilerleme kaydı, bir işte artımlı ilerleme ve doğrulanmadan tamamlandı işaretlememe. Web uygulaması deneyleri genel performans garantisi sayılmadı; örnekteki otomatik commit yaklaşımı repo kuralımıza taşınmadı. |
| S4 | [Anthropic: Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents), 2026-04-08 | Kalıcı oturum kaydı ile model bağlamının ayrılması; yeni modellerde eski harness varsayımlarının tekrar sorgulanması. Hosted hizmet özellikleri bu Markdown skill'inin yapabildiği işler gibi sunulmadı. |

S3'ün GitHub quickstart bağlantısı web aracıyla açılamadı; okunmuş repo örneği gibi kullanılmadı. Önceki sadeleştirme araştırmasındaki YouTube transkriptleri tekrar indirilmedi. Bu eklemenin gerekçesi yukarıdaki birincil yazılara ve mevcut repo sınırlarına dayanıyor.

## Başlangıçtaki boşluk — gözlenmiş hata değildir

`executing-plans` zaten plan, görev doğrulaması ve ledger içeriyor. Ancak deneme bütçesi, aynı başarısızlığı körlemesine tekrar etmeme ve resume sırasında bütçeyi sıfırlamama açık değil. `subagent-driven-development` gövdesinde “bounded rounds” var; kapsamı delegation. `systematic-debugging` teşhis döngüsünü, `verification-before-completion` tamamlanma kanıtını zaten yönetiyor.

Bu nedenle sorun, bütün agent döngülerini yeniden tarif etmek olarak ele alınmadı. Hedef, onaylı inline planın uzun veya tekrarlı yürütülmesindeki kontrol boşluğu. Bu boşluğun canlı agent hatasına dönüştüğü bu oturumda gözlenmedi; aşağıdaki senaryolar henüz çalıştırılmamış değerlendirme vakalarıdır.

## Her değişikliğin gerekçesi

| Dosya / ekleme | Neden eklendi? | Dayanak |
|---|---|---|
| [executing-plans/SKILL.md](../../../skills/executing-plans/SKILL.md): kısa koşullu bölüm | Yalnız istenen repeat-until-verified veya oturumlar arası işte referansı açtırır. Normal görevde yeni hazırlık zorunlu olmaz; mevcut ledger kullanılır. | S1/S2/S4; sadeleştirme hedefi |
| Aynı dosya: `budget-exhausted` output durumu | Bütçe yüzünden durmayı işin tamamlandığı veya dış engel bulunduğu iddiasından ayırır. | S2; yerel durum adlandırması |
| [references/loop-control.md](../../../skills/executing-plans/references/loop-control.md): skill/runner ayrımı | Markdown talimatının scheduler başlatmadığını ve sert kaynak sınırlarını tek başına garanti etmediğini belirtir. | S1/S4; repo bir skill library |
| Referans: goal/check/budget/next alanları | Mevcut plan ve ledger'i yeniden kullanarak başarı koşulunu, kanıtı, kalan hakkı ve sonraki adımı görünür kılar. İkinci bir görev listesi üretmez. | S1–S3 |
| Referans: bütçe seçimi ve sayım | Kullanıcı/runner sınırları öncelikli. İstenen unattended retry için limit yoksa göreve uygun sonlu deneme sınırı önceden belirtilir; başarısız ve yalnız kontrol içeren denemeler de sayılır. | S2; tek evrensel deneme sayısı için kanıt yok, sayım ayrıntısı yerel uyarlama |
| Referans: yetki sınırı | Loop talebi tek başına scheduler, delegation, ücretli model geçişi veya yayım yetkisi sayılmaz; mevcut yetki tekrar istenmez. | Kullanıcı/host yönergeleri; mevcut executor sınırları |
| Referans: action→check→record→decision | Her deneme görünür kontrol sonucuyla yönlenir. Tam log yerine kanıt yolu tutulur; görev yalnız kendi kabul koşulları sağlandığında tamamlanır. | S1–S3 |
| Referans: devam/durma tablosu | Yeni hipotez varsa devam; aynı girdide aynı hatayı körlemesine tekrar etme; bilgi eksikse blocked; sınır dolarsa budget-exhausted; tamamlanmada gerekli final gate'leri koru. | S2/S3; yerel karar tablosu |
| Referans: flakiness istisnası | Aynı kontrolü tekrarlamak kontrollü bir flake deneyinde yeni veri sağlayabilir; bunu yanlışlıkla bütün tekrarları yasaklayan kurala dönüştürmez. | Mevcut systematic-debugging flake yaklaşımı; yerel uyarlama |
| Referans: checkpoint/resume | İlerleme ve bütçe ledger'de kalır. Güncel ağaçla çelişen kanıt yenilenir; değişmemiş tamamlanmış iş yeniden uygulanmaz. Yeni oturum tek başına bütçe yenilemez. | S3/S4; mevcut verification kanıt kapsamı |
| Referans: partial work | Checkpoint oluşturmak için kullanıcı işini resetleme veya otomatik commit etme engellenir. | Repo `AGENTS.md` ve mevcut commit sınırı |
| [routing-manual-test.md](../../../tests/routing-manual-test.md): altı vaka | Normal görev, başarı, bütçe sonu, resume, ilerlemeyen tekrar ve yetersiz kanıt için gözlenebilir beklentiler kaydeder. Sayılar yalnız fixture örnekleridir; skill varsayılanı değildir. | S2/S3; gözlenmeyen başarıyı iddia etmeme |
| [docs/README.md](../../README.md): indeks | Araştırma ve değişiklik gerekçelerini kullanıcı için bulunabilir yapar; runtime skill'e kaynak raporunu yüklemez. | Kullanıcının her eklemeyi gerekçelendirme isteği |

## Doğrulama

- `executing-plans` frontmatter'ı bu eklemede değişmedi; routing açıklaması ve Türkçe cue'lar aynı. v1 sayısı 16 kaldı.
- Skill dosyası 68 → 72 satır, 381 → 425 whitespace kelime oldu: ana dosyaya 44 kelime eklendi. Ayrıntı 48 satırlık koşullu reference'ta; normal görevde yüklenmez.
- `PYTHONDONTWRITEBYTECODE=1 ./tests/run-all.sh`: exit 0 — 16 skill, 32 TR + 49 EN tetikleyici, 81 benzersiz TR cue, 26 router hedefi, 13 optional ve 6 mevcut sentetik senaryo geçti. Bu son sayı yeni canlı davranış vakaları değildir.
- `git diff --check`: exit 0. Eklemenin skill/doküman dosyalarındaki 14 yerel bağlantının hedefleri mevcut. Otomatik repo testleri canlı agent davranışını kanıtlamaz.
- Altı yeni canlı davranış vakası **çalıştırılmadı**; süre, token veya başarı oranında kazanç ölçülmedi.
- Commit, kurulum, scheduler oluşturma ve agent döngüsü çalıştırma bu eklemenin parçası değildir.
