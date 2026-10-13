# superskills

Yazılım geliştirme sürecinde Cursor (ve gerektiğinde Claude Code / Codex) ile çalışırken kullandığım **agent skill** kütüphanesi. Kısaca: “her seferinde aynı disiplini sıfırdan tarif etmek” yerine, mesajına göre doğru moda geçen **on altı tane net workflow** — plan, debug, TDD, PR, git, worktree, subagent, skill yazımı… Hepsi [Agent Skills](https://agentskills.io/specification) formatında; Türkçe tetikleyiciler `description` içinde, gövdeler İngilizce.

Bu repo **uygulama kodu değil**. Ürün burada: `skills/*/SKILL.md`. Gerçek projende `npm test` neyse onu skill’ler ezberlemez; proje kökündeki **`AGENTS.md`** okunur.

---

## Bu işe yarar mı?

Evet, eğer agent ile gerçekten kod yazıyorsan. Fayda şu:

- **Belirsiz mesaj** (“şuna bak”, log yapıştırma) → önce `dev-router`, sonra tek uzman.
- **Net iş** (“plan yaz”, “kök neden”, “PR incele”) → doğrudan ilgili skill; plan modunda debug’a kaymaz.
- **“Bitti”** dediğinde → `verification-before-completion` mantığı: komut koştur, sonra konuş.

Skill sihir değil; iyi mühendislik alışkanlığını her oturumda hatırlatan **checklist + routing**.

---

## 5 dakikada kurulum

**1.** Repoyu klonla.

**2.** Skill’leri makineye bağla — **v1 için bir yöntem seç** (ikisini aynı isimlerle karıştırma):

| Ne yapıyorsun? | Komut |
|----------------|--------|
| Burada skill düzenliyorum (symlink) | `./scripts/link-cursor-skills.sh` |
| “Gerçek” Cursor plugin dizini | `./scripts/install-cursor-plugin.sh` |
| Hepsi bir arada: Cursor + Claude + Codex + optional | `./scripts/link-all-skills.sh` |

Symlink kullanıyorsan repoda değişiklik yaptığında Cursor’da **Reload Window** veya **yeni Agent chat**.

Detay: [docs/plugins.md](docs/plugins.md), [docs/claude-code.md](docs/claude-code.md), [docs/codex.md](docs/codex.md).

**3.** Geliştirdiğin **uygulama** repo’suna kökte `AGENTS.md` koy — şablon: [docs/templates/AGENTS.example.md](docs/templates/AGENTS.example.md). Test, lint, build komutları orada.

Bundan sonra chat’i uygulama klasöründe aç; skill’ler global yüklü (`~/.cursor/skills`), komutlar projeden gelir.

---

## Günlük akış (kafanda canlandır)

```
Fikir net değil     → brainstorming → writing-plans
Plan hazır          → executing-plans / incremental-implementation / spec-driven-development
Test kırıldı        → systematic-debugging → (gerekirse) test-driven-development
PR / diff           → code-review-and-quality
Ship                → git-workflow-and-versioning + verification-before-completion
Paralel / izolasyon → using-git-worktrees, subagent-driven-development
```

“Hangi skill?” diye düşünürsen → `using-agent-skills`. Oturum çöp gitti → `diagnosing-workflow`.

---

## v1 — on altı skill

Tam liste ve Türkçe özet: [skills/CONSOLIDATION.md](skills/CONSOLIDATION.md).

| Aşama | Skill’ler |
|--------|-----------|
| Yönlendirme | `dev-router` |
| Keşif & plan | `brainstorming`, `writing-plans` |
| Kod | `executing-plans`, `incremental-implementation`, `spec-driven-development`, `test-driven-development` |
| Kalite | `systematic-debugging`, `verification-before-completion`, `code-review-and-quality` |
| Git & ortam | `git-workflow-and-versioning`, `using-git-worktrees`, `subagent-driven-development` |
| Meta | `using-agent-skills`, `writing-skills`, `diagnosing-workflow` |

Türkçe örnek tetikleyiciler: `plan yaz`, `kök neden`, `PR incele`, `worktree`, `hangi skill`, `oturum kötü` — tamamı her skill’in YAML `description` alanında (`Turkish cues:`).

---

## Optional (istersen)

`optional/` ayrı katalog: Codex fleet, kota ekranı (`limit`), planı sorgulama (`grilling`), iki eksen review, domain model, vb. Plugin paketine **dahil değil**; `./scripts/link-optional-skills.sh` ile aynı symlink isimlerine bağlanır.

Özet tablo: [optional/README.md](optional/README.md).

---

## Repo haritası

| Klasör | Ne? |
|--------|-----|
| `skills/` | v1 — Cursor plugin buradan |
| `optional/` | Ek skill’ler (MIT parçalar `optional/LICENSE-MIT-*.txt`) |
| `scripts/` | Kurulum |
| `tests/` | Frontmatter, routing, senaryo smoke — `./tests/run-all.sh` |
| `docs/` | Plan/spec şablonları, kurulum notları |
| `.cursor-plugin/` | Plugin manifest |
| `AGENTS.md` | **Bu repoda** agent’a özel operasyon rehberi (skill yazarken) |

`documentations/` yalnızca **lokal** notlar (gitignore; GitHub’da yok).

---

## Bu repoda feature / skill değişikliği

- Plan: `docs/superskills/plans/YYYY-MM-DD-<feature>.md`
- Spec: `docs/superskills/specs/<feature>.md`
- Değişiklikten sonra: `./tests/run-all.sh` (veya `npm test`)
- Cursor’da routing dene: [tests/routing-manual-test.md](tests/routing-manual-test.md)

Agent komutları ve sınırlar: [AGENTS.md](AGENTS.md).

---

## Lisans

Ana skill seti ve repo metinleri kişisel / henüz kök `LICENSE` dosyası yok — fork edip kullanırken kendi koşullarını netleştir. `optional/` altındaki vendored parçalar için [LICENSE-MIT-vendor.txt](optional/LICENSE-MIT-vendor.txt) ve [LICENSE-MIT-mattpocock.txt](optional/LICENSE-MIT-mattpocock.txt).
