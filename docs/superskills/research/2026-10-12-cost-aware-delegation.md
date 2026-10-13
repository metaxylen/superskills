# Maliyet gözeten delegasyon — araştırma ve uygulama, 2026-10-12

## Karar: yeni skill gerekmiyor

Kullanıcının talebi genel bir **ne zaman delegasyon yapılacağı politikası**. Native araçlar zaten agent başlatabiliyor; bizde de plan yürütme, araştırma ve iki eksenli review sahipleri var. Yeni bir `auto-subagents` skill'i aynı karar için yeni routing yüzeyi oluşturur; her görevde kendiliğinden yüklenmesi de garanti değildir.

Uygulama: bu repo'nun `AGENTS.md` dosyasında kısa koşullu yetki ve pointer; ayrıntılar mevcut `subagent-driven-development` skill'inin reference'ında. Araştırma/review kendi uzmanlarında kalır. Başka uygulamalara taşımak için `docs/templates/AGENTS.example.md` bölümünü bilinçli olarak benimsemek gerekir. Başka repo'lar, kişisel/global `AGENTS.md`/`CLAUDE.md` veya host ayarları kendiliğinden değiştirilmedi.

## Güncel birincil kaynaklar

Erişim 2026-10-12. Tarihsiz yaşayan dokümanlarda erişim tarihi kullanıldı; yayın tarihi uydurulmadı.

| Kaynak | Bulgu ve uygulamaya etkisi |
|---|---|
| [OpenAI — Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), yaşayan resmi doküman | Yerel Codex, istek veya geçerli AGENTS/skill talimatıyla delegasyon yapabilir. Okuma ağırlıklı bağımsız işlerde kullanım; yazıların koordinasyon maliyeti; daha fazla token uyarısı. Her hostta proaktif yetki varsayılmadı; Ultra açılmadı. |
| [Claude Code — Subagents](https://code.claude.com/docs/en/sub-agents), yaşayan resmi doküman | Yerleşik delegasyon ve custom agent descriptions zaten var. Fresh context/fork farkı, fork cache avantajı, nested ve concurrency sınırları. Concurrent limit'in toplam session çağrılarını sınırlamadığı açık; bu nedenle yalnız “iki aktif” kuralı yeterli görülmedi. |
| [Anthropic — How and when to use subagents](https://claude.com/resources/articles/subagents-in-claude-code), 2026-04-07 | Küçük/sıralı/aynı dosya işlerinde overhead; politika CLAUDE.md'de, kompleks tekrarlı workflow skill'de. Dosya sayısını otomatik eşik yapmadık. Makalenin eski “agents konuşamaz” genellemesi güncel docs'la uyuşmadığından kopyalanmadı. |
| [Anthropic — Multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), 2025-06-13 | Geniş bağımsız araştırmada fayda; net objective/tools/output/scope handoff'ları; koordinasyon ve token maliyeti. Yazıdaki 15× **chat karşılaştırması**, bizim single-agent task maliyetimiz veya evrensel subagent çarpanı değildir. Sayısal kazançlar taşınmadı. |
| [Purdue araştırmacıları — Cost-Inefficient Behaviors in Coding Agents](https://arxiv.org/html/2609.30725v1), 2026-09-25 ön baskısı | Parent'ın child'ın yaptığı okumaları yinelemesi maliyet kaynağı; bazı retrieval/skill müdahaleleri maliyeti artırabiliyor. Sonuçları farklı modeller/hostlar/işler için garanti saymadık. Hakemli kesin sonuç gibi sunulmadı; inference maliyeti dışında süre/hardware ölçümü yok. |

Bu kaynaklar “her soruda daha çok agent” demiyor. Faydayı handoff, tekrarlanan okuma, raporlama ve integration maliyetiyle karşılaştırmak gerekiyor. Cache ve model tercihi yüzünden yalnız agent sayısından para/kota tasarrufu çıkarmıyoruz.

## GitHub'da gerçekten incelenen kod

[OpenAI Codex commit'i](https://github.com/openai/codex/tree/6c372fbef45f730b6d8aa727b0ec8332365588db), 2026-10-12T12:32:34Z:

- `codex-rs/prompts/src/multi_agent_instructions.rs`: tamamı okundu. Full-history fork model/effort inheritance; overrides için açık talimat; ortak filesystem; host slot sayısına root'un dahil olması.
- `codex-rs/core/src/tools/handlers/multi_agents_v2/spawn.rs`: fork çözümleme ve config bölümleri incelendi. `none`/`all` farkı; öteki hostun CLI flags'iyle karıştırılmadı.
- `codex-rs/core/src/context/world_state/multi_agent_mode_tests.rs`: mod/yetki davranışının test dosyası indirildi; dosyanın tamamı veya bütün repo testleri çalıştırılmış sayılmadı.

`anthropics/claude-code` güncel commit'i `3deb873687379f0c199a69fdaccc65f0865f7a29`, 2026-10-11T19:07:16Z, API'den kontrol edildi. Proprietary runtime'ı açık kaynak repo gibi incelediğimiz iddia edilmiyor; Claude davranışının asıl dayanağı resmi dokümanlar.

Yerel kaynak dosyalarının yolu `/tmp/superskills-delegation-source-path` dosyasında. Model isimleri veya spawn flags'leri skill'e sabitlenmedi; mevcut model/account tercihi korunur.

## Video araştırmasının sınırı

Son ay için resmi YouTube sonuçları arandı. [OpenAI'nin 30 Eylül Bootcamp kaydı](https://academy.openai.com/public/videos/september-30-codex-bootcamp-201-2026-10-01), 1 Ekim yükleme tarihiyle bulundu; web görünümü boş transcript gösterdi, doğrudan fetch 403 verdi ve doğrulanmış YouTube hedefi elde edilemedi. Bu turda o videonun transkriptini çıkardık veya subagent önerilerini öğrendik denmiyor. Konuya doğrudan uyan, son ay tarihini ve birincil video bağlantısını doğruladığımız başka uzman videosu çıkmadı. Önceki Loop Engineering transkriptleri bu konuya yeni kanıt sayılmadı; video varmış gibi başarı uydurulmadı.

## İncelemede bulunan mevcut sorunlar

Bunlar bu turda gözlenmiş model hataları değil, talimatların somut davranışları:

1. `optional/research/SKILL.md` her araştırmada “Spin up a background agent” diyordu. Bir doküman lookup'ında bile ilave çağrı zorunluluğu.
2. Plan executor her task için yeni context, task review ve bounded-round fix döngüsü istiyordu; bütün objective için ortak delegation allocation yoktu.
3. İki eksenli review bütün diff'lerde iki agent tarifliyordu; ufak diff veya eksik spec için maliyet kararı yeterince görünür değildi.
4. Router'daki “Subagents, parallel lanes, delegate chunks” satırı, plansız log/research isteğini approved-plan executor'a gönderebilirdi.

## Her değişikliğin gerekçesi

| Dosya/değişiklik | Gerekçe ve kaynak |
|---|---|
| [AGENTS.md](../../../AGENTS.md): kısa koşullu autonomous delegation request | Her görev için yeni routing skill'i yerine always-read proje politikası. OpenAI resmi yetki mekanizması; mevcut user/host kısıtları öncelikli. Sadece superskills repo'sunda etkin. |
| [delegation-policy.md](../../../skills/subagent-driven-development/references/delegation-policy.md): beş benefit gate | Bağımsız/yoğun/önemli iş; küçük handoff; net değer; sahiplik; bütçe. OpenAI/Anthropic kullanım rehberlerinin distilasyonu. Bir lookup veya script'e child zorunlu değil. |
| Aynı referans: tüm objective boyunca iki work run | Spawn/follow-up/retry sayılır, yeni task/skill/compaction allocation açmaz. İki sayısı **yerel muhafazakâr tercih**, sağlayıcı standardı/kanıtlanmış optimum değil. Kullanıcı farklı allocation belirtebilir. |
| Aynı referans: soft/hard cap ayrımı ve unknown usage | Markdown sert para/kota sınırı değildir. Desteklenen runtime/turn limit'i host uygular; telemetri yoksa tek bounded read-only deneme ve unknown raporu. Concurrency toplam harcamayı sınırlamaz. |
| Aynı referans: nesting/fleet/otomatik reviewer/fallback yasağı | Kullanıcının maliyet isteği; yeni context ve çoğalan çağrıları önleme. Mevcut model seçimi değiştirilmez, daha ucuz seçenek yalnız izin verilmişse. |
| Aynı referans: concise brief, context fork seçimi, scope ownership | Fresh review bağımsızlık sağlar; shared context fork bazı hostta cache avantajı sağlayabilir. Fresh'ın her zaman daha ucuz olduğu söylenmez. Yazı lane'leri ayrı worktree. |
| Aynı referans: duplicate work ve gerçek verification | Parent child'ın bütün işini tekrar yapmaz; kritik iddia/relevant diff gerçek kanıtla kontrol edilir. Tasarruf uğruna gerekli gate atlanmaz. Purdue bulgusu + mevcut verification skill'i. |
| [subagent-driven-development](../../../skills/subagent-driven-development/SKILL.md): optional delegation decision | Approved plan kapsamı korunur; project-authorized kararın da aktivasyon olması sağlanır. Task başına child/reviewer zorunluluğu kaldırılır; parent review yapar. Context inheritance istisnası ile brief kuralı uyumlu. |
| [research](../../../optional/research/SKILL.md): koşulsuz spawn kaldırıldı | Araştırmayı gerektiğinde primary kendisi yapar; faydalı background investigation için mevcut skill açık ve bounded izin verir. Yeni development plan zorunlu olmaz. |
| [code-review](../../../optional/code-review/SKILL.md): iki axis korunur, koşullu lanes | Kalite/spec ayrımı korunur; delegasyon her diff'te zorunlu değil. Ek agent gereksizse aynı kontroller inline. |
| [dev-router](../../../skills/dev-router/SKILL.md): approved plan şartı | Research/debug/review kendi sahibiyle kalır; bir subagent ifadesi tüm işi plan executor'a taşımasın. Description değişmedi. |
| [AGENTS template](../../templates/AGENTS.example.md): opt-in bölüm | Başka uygulamalara bilinçli taşıma; kurulu policy bulunamazsa inline. Global/kişisel talimatlar kendiliğinden değiştirilmez. |
| [EN triggers](../../../tests/routing-triggers-en.tsv): `agent-chosen` | Yeni SDD description branch'i substring gate'inde görünür. TR cues aynı; yeni v1 skill yok. |
| [manual cases](../../../tests/routing-manual-test.md): sekiz decision senaryosu | Tiny/independent/same-file/counter-resume/unknown-usage/no-delegation karşı örnekleri. Bunlar canlı benchmark gibi sunulmadı. |
| docs indeksi ve bu rapor | Kaynak, seçim ve bütün değişikliklerin gerekçesi bulunabilir. Runtime reference'a kaynak makalelerin tamamı yüklenmiyor. |

## Gerçek native subagent kullanımı ve bulgular

Bu turda **bir** native reviewer çağrıldı: `/root/delegation_policy_review`, `fork_turns: none`, model/effort override yok. Brief yalnız altı belirtilmiş policy/skill/template dosyasını read-only incelemesini; maksimum dört material finding; edits/network/nested agents/tests/broad scan yapmamasını istedi. Parent farklı iş olarak kaynak raporunu hazırladı. İki-run allocation'dan bir run kullanıldı; ikinci child veya substantive follow-up yok.

Reviewer'ın iki somut bulgusu:

- “Per task objective” her plan task'ında yeni allocation diye okunabiliyordu. Bütün kullanıcı objective'i boyunca plan task/research/review/resume ortak bütçe olduğu açıklandı.
- Unknown headroom gate'i ile telemetry yokluğunu kabul eden metin çelişiyordu. Exposed yetersiz limit ile unavailable telemetry ayrıldı; ikinci durumda kayıtlı allocation içinde tek bounded read-only pilot ve unknown usage raporu belirtildi.

İkisi primary tarafından kontrol edilip metinde düzeltildi. Bu gerçek faydalı bir review örneği; **n=1**. Agent zaten spawn edilmişken güncellenen politikanın model seçim/routing doğruluğu benchmark'ı değildir. Token/money usage native tool'da görünmedi; tasarruf oranı ölçülmedi. Sekiz manual decision vakası çalıştırılmadı. Yeni pahalı CLI benchmark başlatılmadı; önceki loop benchmark'ı bu değişikliklerin kanıtı sayılmadı.

## Kapsam ve kullanım

Bu repo'da policy otomatik delegasyon kararına izin veriyor; izin, her görevde çağrı yapmak anlamına gelmez. Başka uygulamada template bölümünü o projenin AGENTS/CLAUDE talimatına uygun yerleştirmek gerekir. Claude'ın hangi dosyaları always-read yüklediğiyle Codex'in AGENTS mekanizması aynı varsayılmamalı; policy'yi kullanılan hostun okuduğu talimat dosyasına taşı.

Kullanıcı örneği: “Delegasyon kararını sen ver. Bağımsız ve değerli iş varsa kullan; tüm bu hedef boyunca en fazla iki alt-agent çalışma turu, takipler dahil. Küçük ve birbirine bağımlı işleri kendin yap.” Mevcut izin geçerliyse her dispatch'te tekrar izin sorulmaz. Inline-only talimatı bu tercihi geçersiz kılar.

## Doğrulama

`PYTHONDONTWRITEBYTECODE=1 ./tests/run-all.sh`: exit 0 — 16 skill + plugin; 32 TR + 50 EN trigger; 81 benzersiz TR cue; 26 router hedefi; 13 optional; 6 sentetik routing; offline loop grader kontrolleri. Bu testler native delegation kararını veya para tasarrufunu kanıtlamaz.

Son dosya/link/diff gate'i: `git diff --check` exit 0; 33 yerel bağlantının hedefi mevcut. Commit/kurulum/model-account değişimi yok; kök README kullanıcının önceki snapshot'ıyla aynı tutuldu.
