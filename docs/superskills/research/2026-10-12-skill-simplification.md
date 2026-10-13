# Kaynaklara dayalı skill sadeleştirmesi — 2026-10-12

## Kapsam ve kanıt düzeyi

16 v1 skill tamamen okundu. 13 optional skill'in açıklamaları ve güncellik/kısıt işaretleri tarandı; `codex-fleet` gövdesi tamamen incelendi. Diğer 12 optional skill'in ayrıntılı davranış denetimi bu küçük değişikliğin kapsamına alınmadı.

Aşağıdaki değişiklikler kaynakların birebir emirleri değil, bu depoya uygulanmış ve gerekçesi gösterilmiş uyarlamalardır. Resmî belgeler öncelikli; GitHub örnekleri karşılaştırma, videolar destekleyici görüş olarak kullanıldı. Popülerlik veya kanal görüntülenmesi güvenilirlik kanıtı sayılmadı. Yeni skill, model değişikliği, otomatik commit, kurulum veya yayım yapılmadı.

## İncelenen birincil kaynaklar

| Kimlik | Kaynak ve tarih | Kullanılan ilke / sınır |
|---|---|---|
| D1 | [Eric Provencher / OpenAI: Rethinking skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), 2026-09-11 | Açıklamaları dar tut; göreve göre belge oku; eski model için biriken zorunlu adımları yeniden değerlendir. Model özelindeki görüşler bütün modeller için garanti sayılmadı. |
| D2 | [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), 2026-10-12 erişimi | Gereksiz genel açıklamalar yerine eksik bilgiyi ekle; serbestlik derecesini görevin kırılganlığına göre ayarla; ayrıntıları koşullu yükle. |
| D3 | [Agent Skills specification](https://agentskills.io/specification), 2026-10-12 erişimi | Anlamlı kısa metadata, isteğe bağlı referanslar; gövde için sabit bölüm şeması yok. 1024 karakter bir üst sınır, hedef uzunluk değil. |
| D4 | [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills), 2026-10-12 erişimi | Çağrılan içerik oturumda kalır; dosya her tur tekrar okunmaz. Canlı aktivasyon ve çıktı kalitesi ayrı ölçülür. Ürüne özel YAML alanları başka host'lara taşınmadı. |
| D5 | [OpenAI: Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills), 2026-10-12 erişimi | Pozitif ve negatif kontrol örnekleri; görünür eylem/çıktı üzerinden doğrulama. Statik substring kontrolü canlı routing eval'i değildir. |
| D6 | [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills), 2026-10-12 erişimi | Kullanıcı amacıyla sınırlı workflow; destek dosyalarının ne zaman açılacağını söyle; kullanıcı yönergelerinin önceliğini koru. |
| D7 | [OpenAI: CLI reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli), 2026-10-12 erişimi | `--ignore-rules` yürütme politikası dosyalarını devre dışı bırakır. Doküman ile alpha CLI sürümü bazı bayraklarda farklı; kurulu yardım çıktısı kontrol edildi. |
| L1 | Yerel `AGENTS.md` ve bu konuşmadaki kullanıcı isteği | v1 sayısı 16; commit yalnız istenirse; tam repo test paketi zorunlu; değişiklikler kaynaklı ve ölçülü olmalı. |
| L2 | Kurulu resmî `imagegen/SKILL.md`, 2026-10-12 okundu: `/Users/alparslankiilinc/.codex/skills/.system/imagegen/SKILL.md` | Yerleşik araçta şeffaf çıktı ve alpha koruma; CLI/API fallback yalnız açık istek/onayla. Bu, API'deki her modelin native alpha desteklediği iddiası değildir. |

## GitHub incelemesi — değişmez commit bağlantıları

Güncel branch başları GitHub API ile sorgulandı; aşağıdaki dosyalar indirilip okundu. Tarihler commit tarihleridir, makale tarihi veya tüm dosyaların son düzenlenme tarihi değildir.

| Kimlik | İncelenen dosyalar | Snapshot |
|---|---|---|
| G1 | [Skill authoring](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/SKILL.md), [CI diagnosis](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci/SKILL.md), [Spec to implementation](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/notion-spec-to-implementation/SKILL.md) | `49f948f`, 2026-06-24. Eylül tarihli D1 daha yeni; eski örnekteki her onay adımı taklit edilmedi. |
| G2 | [Skill authoring](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md), [Webapp testing](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/webapp-testing/SKILL.md), [Conditional guidelines](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/internal-comms/SKILL.md) | `dbd4588`, 2026-10-09. Koşullu dosya seçimi ve gerçek görevle değerlendirme örnek alındı; içerik ağacı kopyalanmadı. |
| G3 | [Ecosystem routing](https://github.com/langchain-ai/langchain-skills/blob/16a992f09ab3ccfb642dd4f08d350d833d1990bf/config/skills/ecosystem-primer/SKILL.md), [Eval engineering](https://github.com/langchain-ai/langchain-skills/blob/16a992f09ab3ccfb642dd4f08d350d833d1990bf/config/skills/eval-engineering/SKILL.md) | `16a992f`, 2026-10-02. Framework'e özgü uzmanlık ve reference seçimi incelendi; “INVOKE FIRST” kuralı genel geliştirmeye taşınmadı. |

## Son bir ayın YouTube taraması ve transkriptler

Aralık: 2026-09-12–2026-10-12. Resmî ekip üyeleri ve özgün yayıncılar arandı; üçüncü taraf özetler yalnız keşif için kullanıldı. Yayın tarihini crawl tarihinden ayırdım.

| Kimlik | Video / güvenilirlik | Tarih ve kullanılan bölüm |
|---|---|---|
| V1 | [Thariq Shihipar — Latent Space](https://www.youtube.com/watch?v=IZAlq-V19U8). Anthropic ekip üyesi olduğu [özgün yayın sayfasında](https://www.latent.space/p/thariq) doğrulandı. Birinci elden ürün geliştirme deneyimi. | Yayın sayfası: 2026-09-29. Çıkarılan video transkriptinde yaklaşık 30:12–31:40: model sürümüne göre eski kuralların aşırı kısıtlaması, tekrarlayan hatalara göre yönerge ekleme ve skill eval'leri. Podcast sayfasındaki zamanlar intro farkı nedeniyle farklı. |
| V2 | [7 GPT-6 Astra Rules That Make Codex Work Better — proflead](https://www.youtube.com/watch?v=FESNAh3gNyQ). [Yayıncının video sayfası](https://proflead.dev/videos/gpt-6-astra-codex-prompts-skills-agents-md-FESNAh3gNyQ/) incelendi. Bağımsız anlatım, D1'in açıklaması; yeni teknik iddialar için otorite sayılmadı. | 2026-09-20. 01:47–03:47: odaklı tetikleyici, ilgili referansı seçme, koşulsuz tam test tekrarını azaltma. |

Verilen `yt-captions-md --lang tr,en --timestamps --out ...` aracı iki URL için çalıştırıldı: **2 başarılı, 0 başarısız**. Çıktılar otomatik İngilizce altyazı; teknik adlarda hatalar var. Örneğin `CLAUDE.md` farklı biçimde tanınabiliyor. İddialar resmî belgelerle karşılaştırıldı; bu altyazılar kelimesi kelimesine alıntı için kullanılmadı.

Yerel çıktı dosyaları (repo dışında):

- `/Users/alparslankiilinc/Desktop/transkript/output/Claude Code’s Bitter Lesson Prompts, Harnesses, Mods, and Agents — Thariq Shihipar.md`
- `/Users/alparslankiilinc/Desktop/transkript/output/7 GPT-6 Astra Rules That Make Codex Work Better.md`

LangChain'in yakın tarihli videosu da keşfedildi ancak özgün YouTube sayfası okunamadı, doğrudan site isteği 429 verdi; değişiklik gerekçesine alınmadı. Boris Cherny ve Sam Witteveen için bulunan ilgili eski videolar tarih aralığına uymadığı için yeni kaynak gibi sunulmadı.

## Description değişiklikleri

Ortak gerekçe D1–D3: tekrarları azaltıp işi ve yakın sınırını anlaşılır tutmak. 81 Türkçe cue ve eski 65 EN/TR test satırı korundu. Aşağıdaki amaç değişimleri repo içi çelişkileri gideren yerel uyarlamalardır; canlı routing başarısına dair ölçüm değildir.

`dev-router` açıklamasının eski son cue'sundan sonra gelen “Optional installs” notu, test ayrıştırıcısının son cue'ya bu notu da katmasına neden oluyordu. Not description'dan çıkarıldı; gerçek Türkçe ifade `log yapıştırdım` korundu. Önce/sonra karşılaştırmasında bu eski ayrıştırma hatası normalize edildi.

| Skill | Karakter önce → sonra | Dosyaya özel gerekçe |
|---|---|---|
| [brainstorming](../../../skills/brainstorming/SKILL.md) | 590 → 383 | Genel “can we” tetikleyicisi ve komşu işlerin uzun listesi çıkarıldı; belirsiz özellik tasarımı esas alındı. |
| [code-review-and-quality](../../../skills/code-review-and-quality/SKILL.md) | 553 → 308 | Aynı inceleme isteğinin tekrarları çıkarıldı; diff/PR şartı ve uygulamaya geçmeme sınırı korundu. |
| [dev-router](../../../skills/dev-router/SKILL.md) | 796 → 370 | Görev türlerinin uzun listesi ve optional kurulum notları gövdeye bırakıldı; açık hata teşhisi doğrudan uzmana gider. |
| [diagnosing-workflow](../../../skills/diagnosing-workflow/SKILL.md) | 533 → 332 | Oturum şikâyetlerinin eşanlamlı tekrarları azaltıldı; transkript kanıtı ile uygulama hatası ayrımı korundu. |
| [executing-plans](../../../skills/executing-plans/SKILL.md) | 603 → 321 | Plan uygulama eşanlamlıları azaltıldı; onaylı plan, inline yürütme ve delegation ayrımı korundu. |
| [git-workflow-and-versioning](../../../skills/git-workflow-and-versioning/SKILL.md) | 513 → 279 | “İş bitince kullan” tekrarları çıkarıldı; commit/branch/rebase/PR/release kapsamı korundu. |
| [incremental-implementation](../../../skills/incremental-implementation/SKILL.md) | 609 → 305 | “Birden fazla dosya” gibi geniş tetikleyiciler çıkarıldı; somut özellik veya plan görevi ve dikey dilimler korundu. |
| [spec-driven-development](../../../skills/spec-driven-development/SKILL.md) | 583 → 342 | Spec oluşturma amacı öne alındı; onaylı spec uygulamasında yeniden spec yazdırma önlendi. |
| [subagent-driven-development](../../../skills/subagent-driven-development/SKILL.md) | 589 → 336 | Bağımsız görev tek başına delegation gerekçesi olmaktan çıkarıldı; kullanıcı isteği ve onaylı plan esas alındı. |
| [systematic-debugging](../../../skills/systematic-debugging/SKILL.md) | 655 → 361 | Uzun hata eşanlamlıları ve komşu workflow listeleri azaltıldı; kök neden, stack trace ve regresyon kapsamı korundu. |
| [test-driven-development](../../../skills/test-driven-development/SKILL.md) | 651 → 354 | Genel bütün geliştirme işlerini kapsayan ifade daraltıldı; davranış/test-first/regresyon işi ve mevcut kırmızı test korundu. |
| [using-agent-skills](../../../skills/using-agent-skills/SKILL.md) | 728 → 342 | Sadece “skill/workflow” kelimesinin geçmesine bağlı geniş aktivasyon çıkarıldı; seçim/kurulum soruları ile authoring ayrıldı. |
| [using-git-worktrees](../../../skills/using-git-worktrees/SKILL.md) | 514 → 315 | Genel özellik işi öncesi aktivasyon daraltıldı; istenen izolasyon veya eşzamanlı yazma ihtiyacı esas alındı. |
| [verification-before-completion](../../../skills/verification-before-completion/SKILL.md) | 532 → 300 | Tamamlama tetikleyicileri birleştirildi; güncel kanıt şartı, commit/push/PR öncesi kullanım korundu. |
| [writing-plans](../../../skills/writing-plans/SKILL.md) | 567 → 340 | Plan isteme tekrarları çıkarıldı; onaylı gereksinimler, görev sırası ve doğrulama korundu. |
| [writing-skills](../../../skills/writing-skills/SKILL.md) | 508 → 310 | Skill yazma/düzeltme tekrarları çıkarıldı; bu repo, routing ve SKILL.md doğrulaması korundu. |

## Gövde değişikliklerinin gerekçeleri

| Dosya | Değişiklikler ve gerekçe | Dayanak |
|---|---|---|
| `brainstorming` | Belirsizlikte otomatik ağır yol yerine yeterli en hafif yol; kapsam/risk değişmedikçe alınmış onayı tekrar istememe. Tasarım anlaşması korunur. | D1/D2/D6; yerel uyarlama |
| `writing-plans` | Uygulama repolarına superskills plan yolunu zorlamama; doküman/config görevinde zorunlu RED yerine ilgili kontrol; görev başına etkilenen kontroller + zorunlu proje gate'leri; commit adımı yalnız kullanıcı isterse. Output'taki yol da proje yoluna çevrildi. | D1/D2, L1 |
| `executing-plans` | Her görevde tam suite yerine ilgili kontrol; proje zorunlu gate'leri finalde veya gereken checkpoint'te. TDD davranış değişikliğine ayrıldı; commit otomatik plan emri olmaktan çıkarıldı. | D1/D2, L1 |
| `incremental-implementation` | Yaklaşık 100 satır sınırı yerine doğrulanabilir sonuç; döngüden otomatik commit çıkarıldı; commit isteyen kullanıcıya atomic değişiklik kuralı korundu. “Büyük uncommitted batch” yerine ilgisiz işleri karıştırmama sınırı ve uygun output. | D2, L1; satır eşiği için kaynak bulunmadı |
| `spec-driven-development` | Dosya sayısından dolayı otomatik spec zorunluluğu çıkarıldı; çözümlenmemiş gereksinimler ve anlamlı varsayımlar esas alındı. Yazılı spec onayı korunur. | D1/D2; description ile gövde tutarlılığı |
| `test-driven-development` | Mevcut kodu silip RED'i yeniden kurdurma çıkarıldı; kullanıcı işini koruyarak testin kusuru yakaladığı kanıtlanmalı. Her GREEN'de tam suite tekrarına son; public seam repo örneklerinden seçilir, davranış kararı değişirse sorulur. Config/generation işleri ilgili doğrulamayı kullanır. | D1/D2 + kullanıcı işini koruyan yerel güvenlik düzeltmesi; kaynaklar “kodu sil” emri vermiyor |
| `git-workflow-and-versioning` | Commit sıklığı ve 100 satır hedefi yerine istenen, tek amaçlı commit; kullanıcı entegrasyon tercihini verdiyse seçenekleri yeniden sormama. | L1, D1/D2/D6 |
| `subagent-driven-development` | Görev bağımsızlığı tek başına ajan başlatma yetkisi sayılmaz; kullanıcı delegation isteği aranır. | Konuşmanın delegation sınırı; description/gövde tutarlılığı |
| `dev-router` | “Mevcut spec'i uygula → spec yazma skill'i” çelişkisi düzeltildi; yeni spec → spec skill'i, onaylı spec'ten görev çıkarma → plan skill'i. Somut küçük iş için zorunlu brainstorm→plan zinciri kaldırıldı. Kod yazmayan handoff için onay isteme çıkarıldı. | Yerel spec skill'inin mevcut işi, D1/D6 |
| `using-agent-skills` | İkinci 16'lı katalog ve aynı karar diyagramı yerine kaynak dosyalarına pointer. İki eşzamanlı ana skill yerine adım başına bir tane. Genel varsayım/uyarı şablonları bir cümlede toplandı; değişmemiş skill'i tekrar okuma yerine yüklü içeriği kullanma. | L1, D1/D3/D4; çakışan yerel kurallar |
| `using-git-worktrees` | Gerekli `.gitignore` düzenlemesi doğrudan commit edilmez; commit kullanıcı isterse. | L1 |
| `writing-skills` | Sadece gerekli bölümler; sabit “use when” kalıbı yerine iş/aktivasyon/sınırın anlaşılır olması; yalnız yakın iş için owning skill belirtme. Install dokümanını sadece kurulum yüzeyi değişirse güncelleme; örtüşen skill'leri okuma; gözlenmeyen RED vakasını gerçek agent hatası gibi sunmama; pozitif/negatif örnekler ve statik/canlı test ayrımı. Tekrarlanan frontmatter komutu yerine zaten zorunlu bütün test gate'i. | D1–D5, L1 |
| `verification-before-completion` | Proje gate'leri korunur; hedef test yalnız kendi kapsamını kanıtlar; girdileri değişmemiş kanıt tekrar kullanılabilir. Lint sonucu build sonucu yerine sunulamaz. Başka ajan sonucu için doğrudan “başarılı” demek yerine güncel ağaçla kanıtı karşılaştırma. | D1/D5, L1; kanıtsız tamamlandı iddiası hâlâ yasak |

`systematic-debugging`, `code-review-and-quality` ve `diagnosing-workflow` gövdeleri değiştirilmedi; yalnız açıklamaları kısaltıldı. Teşhis fazları, review kanıtı ve transkript sınırları için gereksiz olduklarını gösteren kanıt yoktu.

## codex-fleet: taşıma ve doğrulanmış güncellemeler

| Dosya / alan | Ne değişti, neden? | Dayanak |
|---|---|---|
| `SKILL.md` | 639 satırlık gövde 53 satırlık giriş/koşullu seçim dosyasına ayrıldı. Genel CLI işi için görsel reçeteleri okunmaz. Açıklama 223 karaktere indi; sadece CLI istenen iş ve native araç ayrımı yapıldı. Model/effort tercihleri silinmedi, runtime'da kaldı. | D1–D3/D6, G1/G2 |
| `references/runtime.md` | Önceki platform/varsayılanlar taşındı; eski minimum CLI sürüm listesi yerine kurulu yardım kontrolü; stderr'i kaybetmek yerine logda koruma. | D7 + yerel `codex --version`, `codex exec --help`; başarısızlığı görünür tutma uyarlaması |
| `references/tasks.md` | Genel exec/resume/approval/hata adımları taşındı. `--full-auto` hakkında tüm sürümlere genellenen ifade yerine kurulu yardım; sınırsız paralellik yerine host/hesap sınırları. stderr kaydı korundu. | D7; sürüm çelişkisi aşağıda; mevcut fleet metni zaten kaynak sınırlarını kabul ediyordu |
| `references/image-references.md` | `-i`, `--` ayracı ve bağımlı görsel zinciri aynen ayrı dosyaya taşındı. Kod-only işte gereksiz, referanslı görsel işinde gerekli. | D1–D3; bu örnekler yeniden gerçek görsel çağrısıyla test edilmedi |
| `references/image-generation.md` | Görsel ayrıntıları taşındı; uzun reference için içerik dizini eklendi. `--ignore-rules` varsayılan reçeteden çıkarıldı. Şeffaflıkta zorunlu chroma-key yerine yerleşik araç+alpha kontrolü. Boyut/kalite/batch kelimeleri API fallback için yeterli gerekçe sayılmadı. >100 KB başarı eşiği, %99 metin doğruluğu, geniş otomatik refusal listesi ve sabit maliyet/limit çarpanları çıkarıldı. Tool sonucu ve görsel inceleme esas. | D2/G2 (TOC), D7, L2; bu sayısal kalite/maliyet iddiaları için güvenilir güncel dayanak bulunmadı |
| `references/fleets.md` | Lane ownership, izolasyon, integration ve kanıt kontrolleri ayrı dosyaya taşındı. Orijinal ayrıntılar korundu; gerçek çok-lane benchmark yapılmadı. | D1–D3/G2; çalışma ayrıntıları korunarak koşullu yükleme |
| Root kaynak pointer'ları | Her reference doğrudan root'tan bağlı; hangi işte açılacağı ve script yolunun skill kökünden çözüleceği yazıldı. Kullanıcı/host yetkilerinin önceliği, sessiz API geçişi olmaması ve çıktı doğrulama özetlendi. | D3/D6, L1/L2; taşımanın erişilebilirliğini korumak için |
| `optional/README.md` | Yeni reference düzeni ve mevcut dizin symlink'inin hepsini kapsadığı açıklandı. | L1 + mevcut `link-optional-skills.sh` davranışı |

Önemli sürüm farkı: kurulu CLI `0.162.0-alpha.17.2`, yardımında `--approve-for-me` var, `--full-auto` yok. D7 hâlâ `--full-auto`yu deprecated uyumluluk bayrağı olarak anlatıyor. Bu nedenle “bütün sürümlerde yok” veya “bütün sürümlerde var” iddiası yapılmadı; eski sürüm sayıları yerine help kontrolü yazıldı. Ağ/API çağrısı yapan bir Codex görevi başlatılmadı.

L2, yerleşik aracın transparan talebi ile CLI model yeteneklerinin ayrı olduğunu gösteriyor. Bu değişiklik `gpt-image-2` API'sinin native alpha desteği olduğu iddiasını eklemez. Kullanıcı onayı gerektiren API/model geçişi korundu.

## Test ve doküman eklemeleri

- `tests/routing-triggers-en.tsv`: Her v1 açıklamadan bir ayırt edici pozitif ifade, toplam 16 yeni satır. Eski EN/TR satırları ve Türkçe cue'lar korundu. Amaç description'dan gerekli işaretlerin kaybolmasını yakalamak (D3/D5).
- `tests/optional-routing-triggers.tsv`: CLI isteğine odaklanan `run Codex CLI` satırı; mevcut `codex exec` korunur (D1/D5).
- `tests/routing-manual-test.md`: 13 pozitif/negatif yakın örnek ve canlı değerlendirme yöntemi eklendi; özellikle yeni spec/mevcut spec, meta/authoring, inline/delegation, açıklama/exec ve native image/CLI ayrımları (D4/D5).
- Bu rapor: kullanıcı her değişikliğin gerekçesini istediği için kaynak, tarih, snapshot, ölçüm ve sınırlar kaydedildi. Runtime skill gövdelerine araştırma notları yüklenmedi.
- `docs/README.md`: raporu bulunabilir kılan indeks bağlantısı; proje plan yolu anlatımı güncellenen skill ile tutarlı hale getirildi.

## Ölçüm ve doğrulama

- V1 description toplamı: **9524 → 5298 karakter (%44.4 azalma)**.
- V1 SKILL.md toplamı: **7851 → 7149 whitespace ile ayrılmış kelime (%8.9 azalma)**. Tokenizer ölçümü veya hız benchmark'ı değildir.
- `codex-fleet` root: **639 → 53 satır**. CLI-only işte root + runtime + tasks = 183 satır; diğer içerik gerektiğinde okunur. Satır sayısı gerçek token/süre kazancı garantisi değildir.

- Başlangıçta `./tests/run-all.sh` exit 0: 16 skill, 32 TR + 33 EN tetikleyici, 81 benzersiz TR cue, 26 router hedefi, 13 optional skill, 6 synthetic senaryo.
- Düzenlemeler sonrası `./tests/run-all.sh` exit 0: 16 skill, 32 TR + 49 EN tetikleyici, aynı 81 TR cue, aynı router/optional/synthetic sayıları.
- V1 ve codex-fleet Markdown dosyaları, yeni reference pointer'ları, doküman indeksi ve bu raporun yerel bağlantıları kontrol edildi; eksik dosya hedefi yok.
- Root `README.md` görev başında zaten değiştirilmişti; başlangıç snapshot'ıyla byte-for-byte eşitliği doğrulandı, kullanıcı değişikliği korunuyor.
- Canlı Claude/Cursor/Codex routing karşılaştırması ve üretim performans benchmark'ı **çalıştırılmadı**. 13 manuel senaryo hazır; statik başarı model davranışı iyileşti iddiasına çevrilmedi.
- Yeni sohbet veya pencere reload'u metadata'nın yeniden yüklenmesi için gerekir. Commit/push/release/kurulum yapılmadı.

## Bilerek büyütülmeyen işler

16'lı skill seti birleştirilmedi veya genişletilmedi. Diğer optional gövdeler topluca yeniden yazılmadı. `codex-fleet`in model/effort ve standard-tier tercihleri değişmedi. Platforma bağlı resume, fiyat oranı, concurrency ve görsel boyut ayrıntılarının tamamı yeniden smoke-test edilmedi; bunlar için runtime help/tool yönergeleri esas alınmalı. Geniş değişiklik için ölçülmüş başarısızlık ve ayrı inceleme gerekir.
