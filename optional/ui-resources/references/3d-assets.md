# 3D asset sources

Verified 2026-10-14 by fetching vendor pages and calling the APIs directly. Licenses live per source or per model; read the license at approval time. Source of each claim is in the last column.

## Approval rule (mandatory)

**Never download, copy into the project, or reference an asset until the user approves it.** Searching and listing are allowed without asking. For each candidate show:

1. Name, source and direct page URL (preview link when available)
2. License, whether attribution is required, and the exact credit line if so
3. Polygon count, file size, format
4. One sentence on why it fits the design

Offer one to three candidates, then wait for an explicit yes. A yes covers that asset only. After approval, record source URL, author and license in the project (for example `ASSETS.md`) and add the credit if required.

Skip licenses that do not fit the project: NonCommercial for commercial work, NoDerivs when the model must be modified, ShareAlike when the project cannot comply, royalty-free terms you have not read. When unsure, say so in the approval message.

## A. Searchable by API (an agent can query without a login)

| Source | License | How | Checked |
|---|---|---|---|
| [Sketchfab](https://sketchfab.com/3d-models?features=downloadable&sort_by=-likeCount) | Per model: CC0, CC BY, BY-SA, BY-ND, BY-NC, BY-NC-SA, BY-ND, Free Standard, Standard, Editorial | `GET https://api.sketchfab.com/v3/search?type=models&downloadable=true&q=<term>&license=cc0&sort_by=-likeCount`; results carry `license.label`, `uid`, `viewerUrl`, `faceCount`. License slugs: `GET /v3/licenses`. Download: `GET /v3/models/{uid}/download` with the user's OAuth bearer token (short-lived glTF zip link, about 300 s, do not cache). Token comes from the user through an environment variable, never pasted in chat | Live calls; [download docs](https://sketchfab.com/developers/download-api/downloading-models). KitBash bought Sketchfab from Epic on 2026-08-10 ([Epic announcement](https://www.epicgames.com/site/news/kitbash-acquires-artstation-and-sketchfab)); search and listing still worked on 2026-10-14, but API and free-download policy after the sale is unannounced, so recheck before relying on it |
| [Smithsonian 3D](https://3d.si.edu) on Sketchfab | CC0 | Same Sketchfab search; for example `q=smithsonian&license=cc0` returned Apollo 11 Command Module, Figure of a Dancer, Side Chair under user `Smithsonian`. Also the [Open Access API](https://api.si.edu/openaccess/api/v1.0/search) (works with an api.data.gov key; `DEMO_KEY` returned 200 but is rate-limited) | Live calls |
| [Poly Haven](https://polyhaven.com/models) | CC0, no attribution (apps built on the API should credit "Powered by Poly Haven") | `GET https://api.polyhaven.com/assets?t=models`; `GET /files/{id}` gives glTF, FBX, USD at 1k/2k/4k; `GET /info/{id}` gives author. Also HDRIs and textures | Live calls; [API repo](https://github.com/Poly-Haven/Public-API) |
| [BlenderKit](https://www.blenderkit.com) | Free assets are `royalty_free`, which is not CC0; read BlenderKit's royalty-free terms before proposing one | `GET https://www.blenderkit.com/api/v1/search/?query=chair+asset_type:model+is_free:true`; search returned 1,807 free chair models. Downloading needs a BlenderKit account (not tested) | Live call for search only |
| [Gobkit free pack](https://gobkit.com/freebies) | CC0 stated per model in the JSON | `GET https://gobkit.com/api/free` returns packs with model URLs, `rigged`, animation ranges, `license`. Only about 99 models and a commercial vendor's sampler, so treat as a small bonus, not a library | Live call |
| [Khronos glTF-Sample-Assets](https://github.com/KhronosGroup/glTF-Sample-Assets) | Per model; read each model's README (example: CC BY 4.0) | `gh api repos/KhronosGroup/glTF-Sample-Assets/contents/Models/model-index.json` | Repo page and API |

## B. Verified, manual download

| Source | License | Notes | Checked |
|---|---|---|---|
| [Kenney](https://kenney.nl/assets?q=3d) | CC0, credit optional | Low-poly kits, GLB/GLTF, OBJ, FBX per ZIP | [Kenney support page](https://kenney.nl/support) |
| [KayKit](https://kaylousberg.itch.io) (Kay Lousberg) | CC0 on the pages checked (Resource Bits pack) | Stylized kits and animated characters, free on itch.io; check each pack's license line | itch.io page |
| [Quaternius](https://quaternius.com) | Quaternius Asset License v1.0, not CC0: free commercial use, no attribution, but no reselling or redistributing the assets themselves | Characters, nature, buildings, animated packs | [License page](https://quaternius.com/license.html) |
| [ambientCG](https://ambientcg.com) | CC0 | Mostly PBR materials and HDRIs; some models | Site page |
| [NASA 3D Resources](https://science.nasa.gov/3d-resources/) ([GitHub mirror](https://github.com/nasa/NASA-3D-Resources)) | Free to download; usage follows NASA media guidelines, read them first | Spacecraft, planets; glb among formats | Site page |
| [OpenGameArt](https://opengameart.org) | Mixed (CC0, CC-BY, OGA-BY, GPL); shown on each asset's page | The 3D filter plus a CC0 license filter lists assets; check each page | Site search page responded; license claim from [search summary](https://app.cinevva.com/guides/free-3d-model-sites), not read per asset |

## C. Partly verified or use with care

| Source | Why careful |
|---|---|
| [Poly Pizza](https://poly.pizza) | Site is up and hosts archived Google Poly models; licenses are reported as mostly CC BY with some CC0, so read each model's license. I could not read its license page |
| [Objaverse](https://huggingface.co/datasets/allenai/objaverse) | Research dataset. Dataset license is ODC-By (verified on Hugging Face); each object keeps its own license (CC BY, BY-NC, BY-SA, CC0). Not suitable for production use without per-object checks |
| Sloyd, Meshy, Mixos, opensource3dassets | Aggregators or AI-generator catalogs. Claims seen only in search summaries (Sloyd CC BY 4.0, Mixos mirrors Poly Haven CC0); not verified, prefer the original source |
| Mixamo | Characters and animations; needs an Adobe account; page did not load, terms unread |
| CGTrader, TurboSquid, Free3D | Free sections have mixed licenses; terms unread |

## Practical notes

- Popular Sketchfab models are often heavy (the first three "robot" results sorted by likes had 9k to 209k faces) and many are CC BY. Check `faceCount` and the license before proposing one.
- For web use prefer glTF/GLB; keep hero models light (rule of thumb, not a sourced limit) and say so when proposing a heavy one.
- Poly Haven HDRIs light a Three.js scene without any model.
- Start with Poly Haven, Kenney, KayKit and Smithsonian: all CC0 and clean to approve. Reach for Sketchfab when the design needs something specific.
