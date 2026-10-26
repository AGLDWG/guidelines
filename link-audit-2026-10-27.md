# Guideline link and standards audit — 27 October 2026

Scope: `PID-IRI-Guidelines-v2.2.md` on local branch `iso-reference-update`, including the uncommitted ISO citation clarification. No additional guideline edits were made for this audit. Raw results and source fingerprint are in [link-audit-2026-10-27.json](link-audit-2026-10-27.json). Line numbers below refer to this audited file.

56 distinct linked external URLs were checked: 48 returned HTTP 200 after redirects, five returned HTTP 404, two failed DNS resolution, and one returned HTTP 403. These are observations from this environment, not permanent availability claims. The 403 is the real ISO 19135:2026 publisher page, independently retrieved through the web research tool, so it is not classified as a broken reference. Example namespace strings in code are excluded. Four local image references (two images, each linked and embedded) exist. Internal fragment checks found eight problematic link occurrences across seven distinct targets, plus three malformed HTML reference anchors.

## Broken external destinations

| Guideline line(s) | Destination / result | Recommended handling |
| --- | --- | --- |
| 237 | `https://data.gov.au/dataset/rottnest-ferries-underway-temperature` — 404 | Replace with a verified real dataset example, or explicitly make the example hypothetical. No equivalent dataset destination was established in this audit. |
| 489 | `http://test.linked.data.gov.au/def/status` — DNS failure, also over HTTPS | The guideline's own `https://linked.data.gov.au/def/reg-statuses/…` links work. Update this bibliography entry to the status vocabulary's production PID; verify the scheme landing page before applying. |
| 491 | GOV.UK path `designing-IRI-sets-for-the-uk-public-sector` — 404 | The original is [Designing URI sets for the UK public sector](https://www.gov.uk/government/publications/designing-uri-sets-for-the-uk-public-sector). Correct both the title and URL. This is a URI/IRI transcription error. |
| 512 | `http://metadata-standards.org/11179/` — 404, also over HTTPS | Replace the dead series index with an authoritative ISO reference. The citation does not identify a part or edition; do not silently change it to one specific part. See the standards table. |
| 523 | W3C path `/TR/coolIRIs/` — 404 | Correct to [Cool URIs for the Semantic Web](https://www.w3.org/TR/cooluris/), retaining its 2008 Interest Group Note identity. Correct the title too. |
| 525 | W3C wiki path `223_Best_Practices_IRI_Construction` — 404 | Correct to [223 Best Practices URI Construction](https://www.w3.org/2011/gld/wiki/223_Best_Practices_URI_Construction). The original survives as a read-only archived wiki, not a W3C Recommendation. |
| 583 | `http://lode2.linked.data.gov.au` — DNS failure, also over HTTPS | Remove or qualify the claim about this service; agree a maintained replacement in the rebuilt publication workflow. No replacement is asserted here. |

The three URI/IRI mistakes should be repaired as exact citation corrections. General discussion of IRIs elsewhere need not change.

## Withdrawn, superseded, updated or misdescribed standards

| Citation | Verified status and evidence | Recommended handling |
| --- | --- | --- |
| ISO 19135-1:2015 | [Withdrawn and replaced by ISO 19135:2026](https://www.iso.org/standard/54721.html). [Successor published February 2026](https://www.iso.org/standard/87753.html). | Already addressed by the local draft: retain the historical basis and describe the successor separately. Do not claim alignment without reviewing roles and procedures. |
| ISO/IEC 11179, labelled ISO-2015 | The guideline cites a multipart series without a part or edition. For example, [Part 1:2023](https://www.iso.org/standard/78914.html) is published and supersedes Part 1:2015. This does not establish the status of every part. | Clarify what was intended before updating the edition. It is historical in the v2.2 changelog, not a reason to move this guideline back to ISO 11179. |
| HTML 5.2, W3C-2017 | Formally [superseded on 28 January 2021](https://www.w3.org/TR/2021/SPSD-html52-20210128/). The cited generic `/TR/html/` now redirects to the [WHATWG HTML Living Standard](https://html.spec.whatwg.org/multipage/), not the dated 2017 document. | Choose deliberately: use the dated superseded snapshot for historical accuracy, or update the citation to the Living Standard for current implementation guidance. Appendix A recommends HTML5 generally; this is not an automatic mandate to change resource delivery. |
| RFC 2616, IETF-1999 | [Obsoleted by RFCs 7230–7235](https://datatracker.ietf.org/doc/rfc2616/). Current replacements for that suite include [RFC 9110: HTTP Semantics](https://datatracker.ietf.org/doc/rfc9110/), [RFC 9111: Caching](https://datatracker.ietf.org/doc/rfc9111/), and [RFC 9112: HTTP/1.1](https://datatracker.ietf.org/doc/rfc9112/). RFC 9112 also lists RFC 9931 as an update. | The bibliography marks RFC 2616 “Not used”; remove it if still unused. If HTTP semantics are needed, cite the appropriate current document rather than mechanically replacing a whole protocol suite with a single RFC. |
| RFC 2119, IETF-1997 | Still Best Current Practice, [updated by RFC 8174](https://www.rfc-editor.org/info/rfc2119/). Not withdrawn or obsolete. | Retain it and consider adding RFC 8174 and the standard BCP 14 wording about uppercase keywords in the conformance section. |
| STD 68 / RFC 5234, IETF-2008 | Still an Internet Standard, [updated by RFC 7405](https://www.rfc-editor.org/info/rfc5234/). | Retain the base reference. Cite the extension if adopting its case-sensitive literal notation; it is not a compulsory replacement. |
| RFC 6570, IETF-2012 | [Proposed Standard, URI Template](https://www.rfc-editor.org/info/rfc6570/). No obsolescence indicated on its RFC Editor record. | The guideline calls it “IRI Template”; correct the title if retained. It is marked “Not used”, so removal is another small cleanup option. |
| RDF 1.1 Concepts, W3C-2014 | Published as a [W3C Recommendation](https://www.w3.org/TR/rdf11-concepts/), not merely the January 2014 Proposed Recommendation named in the bibliography. [RDF 1.2 is a Candidate Recommendation Snapshot](https://www.w3.org/TR/rdf12-concepts/) and explicitly points to RDF 1.1 as its latest Recommendation. | Keep RDF 1.1 as the stable citation and correct its publication stage/date to Recommendation, 25 February 2014. No automatic RDF 1.2 migration. |
| RDF Schema 1.1, W3C-2014b | [Published Recommendation](https://www.w3.org/TR/rdf-schema/); linked document remains available. | Retain. |
| Organization Ontology, W3C-2014c | [Published Recommendation](https://www.w3.org/TR/vocab-org/); linked document remains available. | Retain. |
| DCMI Terms, DCMI-2012 | The old path returns a redirect document; the [current DCMI Recommendation](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) is dated 20 January 2020. | Update to its canonical URL if retaining the reference. It is marked “Not used”. |

## Internal references and citation errors

| Line(s) | Issue | Repair |
| --- | --- | --- |
| 13 | `#1-Preface` differs in case from generated `#1-preface` | Normalize the fragment to the heading slug. |
| 51, 146 | `#ref-AGLDWG-2021` is used, but no bibliography entry/anchor exists | Add the intended Registry Roles Vocabulary reference, pointing to its verified production PID. |
| 58, 517 | `#ref-PC-2017` is missing because the bibliography uses `href="ref-PC-2017"` instead of an anchor | Use `id` or `name`; the current href points at a nonexistent local file. |
| 81, 493 | The text links to `#ref-CAR2-17`; the intended entry is CAR-2017, itself incorrectly written as an href | Correct the fragment and create the actual anchor. |
| 229 | “Section 9” / `#9-second-level-registers` points to no heading | Correct to Section 8.4 / `#84-second-level-registers`. |
| 239, 533 | `#ref-W3C-2016` has no anchor; bibliography uses a relative href and an unclosed `<a>` | Replace with a closed named/id anchor. The external HashVsSlash wiki itself returns 200. |
| 389 | `#ref-17` has no entry | The surrounding text names the Registry Ontology; use existing `#ref-REY-2012`. |
| 192 | The AGLDWG-2018b status-vocabulary label links to `#ref-AGLDWG-2018` (governance) | Point it to `#ref-AGLDWG-2018b`. This link resolves but to the wrong reference. |
| 67, 81, 521 | Citation text says TBL-2009, but its target/entry say TBL-2006 | Reconcile the intended dated version rather than inferring one from a mutable page. |

The new legacy ISO anchor remains present. The two workflow/status diagram files exist. As an adjacent repository issue outside the guideline itself, README links to v2.2 and v2.1 use `PID-URI-…` although those files are named `PID-IRI-…`.

## Resolving but misleading or requiring review

- The W3C Linked Data overview at `https://www.w3.org/standards/semanticweb/data` redirects to the general W3C standards index. This is a semantic dead end, despite HTTP 200. Select a specific official Linked Data overview; the separately cited Berners-Lee Linked Data page still resolves.
- The catalogue, AGLDWG pages, production registry-role terms and all twelve linked status terms returned 200. This is useful availability evidence, not verification that the 2021 submission forms or approval/publication promises remain operational. Modern web app shells were not tested end to end.
- The old purl.org, Productivity Commission and RVA links redirect successfully. These are optional canonical-URL cleanups, not broken citations. Preserve persistent identifiers where they are intentional rather than replacing all of them with their current hosting locations.
- The DOI article and Registry Ontology document return 200. Their age alone is not a reason to replace them; the Registry Ontology's role in the rebuilt PID model is a separate substantive review.
- ISO's newer page blocked the automated Python request with HTTP 403 but its publication metadata was accessible through the web research tool. Do not confuse access controls with link rot.

## Repair progress after the audit

The three URI/IRI title-and-URL mistakes and the resolvable internal reference/citation errors have now been repaired in the local guideline draft. This includes a missing Registry Roles Vocabulary bibliography entry; malformed citation anchors and the Organization Ontology link; incorrect section numbers; the wrong status-vocabulary reference target; consistent TBL-2006 labels matching the source page's original publication date; and the README links to versions 2.1 and 2.2. All 70 Markdown fragment links resolve, HTML anchors are closed, and local file targets exist. The inventory and line numbers above remain the original audit snapshot.

One additional reference needs an editorial decision: Section 8.4 mentions Figure 3, but v2.2 contains no Figure 3. Version 2.1 embeds `workflow-implementation.png` as Figure 3; that image describes a legacy implementation workflow. Restoring it as current guidance would go beyond link repair, so the mention is unchanged pending discussion with Nick. Other service and standards-adoption findings remain deferred.

## Suggested small maintenance scope

Repair the exact URI/IRI URL/title mistakes, internal anchors, missing roles-vocabulary reference and wrong-section links. Retain historical ISO provenance. Treat HTML adoption, replacement service claims, obsolete HTTP citations and multipart ISO 11179 references as explicit editorial decisions. Do not bulk-upgrade standards or rewrite the emerging PID workflow as part of link repair.

## Complete external request inventory

HTTP results include redirects. “DNS/error” means the exception is recorded in the JSON. The ISO 403 is inconclusive for the automated probe.

| Line(s) | Original linked URL | HTTP | Final destination |
| --- | --- | --- | --- |
| 1 | <https://www.linked.data.gov.au> | 200 | <https://www.linked.data.gov.au> |
| 7 | <https://www.linked.data.gov.au/contact> | 200 | <https://www.linked.data.gov.au/contact> |
| 42 | <https://github.com/AGLDWG/guidelines> | 200 | <https://github.com/AGLDWG/guidelines> |
| 46, 487 | <https://www.linked.data.gov.au/governance> | 200 | <https://www.linked.data.gov.au/governance> |
| 96 | <https://catalogue.linked.data.gov.au> | 200 | <https://catalogue.linked.data.gov.au> |
| 104, 607 | <http://catalogue.linked.data.gov.au> | 200 | <https://catalogue.linked.data.gov.au/> |
| 115, 237 | <https://data.gov.au> | 200 | <https://data.gov.au> |
| 115 | <http://purl.org> | 200 | <https://purl.archive.org/> |
| 115 | <https://w3id.org/> | 200 | <https://w3id.org/> |
| 125 | <https://linked.data.gov.au/def/reg-roles> | 200 | <https://agldwg.github.io/reg-roles/> |
| 129 | <https://linked.data.gov.au/def/reg-roles/control-body> | 200 | <https://agldwg.github.io/reg-roles/control-body> |
| 130 | <https://linked.data.gov.au/def/reg-roles/register-owner> | 200 | <https://agldwg.github.io/reg-roles/register-owner> |
| 131 | <https://linked.data.gov.au/def/reg-roles/register-manager> | 200 | <https://agldwg.github.io/reg-roles/register-manager> |
| 132 | <https://linked.data.gov.au/def/reg-roles/register-user> | 200 | <https://agldwg.github.io/reg-roles/register-user> |
| 133 | <https://linked.data.gov.au/def/reg-roles/registry-manager> | 200 | <https://agldwg.github.io/reg-roles/registry-manager> |
| 134 | <https://linked.data.gov.au/def/reg-roles/submitting-organization> | 200 | <https://agldwg.github.io/reg-roles/submitting-organization> |
| 135 | <https://linked.data.gov.au/def/reg-roles/submitter> | 200 | <https://agldwg.github.io/reg-roles/submitter> |
| 137 | <https://www.linked.data.gov.au/join> | 200 | <https://www.linked.data.gov.au/join> |
| 194 | <https://linked.data.gov.au/def/reg-statuses/accepted> | 200 | <https://agldwg.github.io/reg-statuses/accepted> |
| 195 | <https://linked.data.gov.au/def/reg-statuses/deprecated> | 200 | <https://agldwg.github.io/reg-statuses/deprecated> |
| 196 | <https://linked.data.gov.au/def/reg-statuses/retired> | 200 | <https://agldwg.github.io/reg-statuses/retired> |
| 197 | <https://linked.data.gov.au/def/reg-statuses/superseded> | 200 | <https://agldwg.github.io/reg-statuses/superseded> |
| 198 | <https://linked.data.gov.au/def/reg-statuses/unstable> | 200 | <https://agldwg.github.io/reg-statuses/unstable> |
| 199 | <https://linked.data.gov.au/def/reg-statuses/valid> | 200 | <https://agldwg.github.io/reg-statuses/valid> |
| 200 | <https://linked.data.gov.au/def/reg-statuses/experimental> | 200 | <https://agldwg.github.io/reg-statuses/experimental> |
| 201 | <https://linked.data.gov.au/def/reg-statuses/stable> | 200 | <https://agldwg.github.io/reg-statuses/stable> |
| 202 | <https://linked.data.gov.au/def/reg-statuses/notAccepted> | 200 | <https://agldwg.github.io/reg-statuses/notAccepted> |
| 203 | <https://linked.data.gov.au/def/reg-statuses/invalid> | 200 | <https://agldwg.github.io/reg-statuses/invalid> |
| 204 | <https://linked.data.gov.au/def/reg-statuses/reserved> | 200 | <https://agldwg.github.io/reg-statuses/reserved> |
| 205 | <https://linked.data.gov.au/def/reg-statuses/submitted> | 200 | <https://agldwg.github.io/reg-statuses/submitted> |
| 237 | <https://data.gov.au/dataset/rottnest-ferries-underway-temperature> | 404 | <https://data.gov.au/dataset/rottnest-ferries-underway-temperature> |
| 489 | <http://test.linked.data.gov.au/def/status> | DNS/error | — |
| 491 | <https://www.gov.uk/government/publications/designing-IRI-sets-for-the-uk-public-sector> | 404 | <https://www.gov.uk/government/publications/designing-IRI-sets-for-the-uk-public-sector> |
| 493 | <https://doi.org/10.5334/dsj-2017-013> | 200 | <https://datascience.codata.org/articles/10.5334/dsj-2017-013> |
| 496 | <http://www.dublincore.org/documents/dcmi-terms/> | 200 | <https://www.dublincore.org/documents/dcmi-terms/> |
| 499 | <http://tools.ietf.org/html/rfc6570> | 200 | <https://www.rfc-editor.org/info/rfc6570/> |
| 502 | <http://www.ietf.org/rfc/rfc2616> | 200 | <https://www.rfc-editor.org/info/rfc2616/> |
| 504 | <http://www.ietf.org/rfc/rfc2119> | 200 | <https://www.rfc-editor.org/info/rfc2119/> |
| 506 | <https://tools.ietf.org/html/std68> | 200 | <https://www.rfc-editor.org/info/std68/> |
| 508 | <https://www.iso.org/standard/54721.html> | 200 | <https://www.iso.org/standard/54721.html> |
| 510 | <https://www.iso.org/standard/87753.html> | 403 | <https://www.iso.org/standard/87753.html> |
| 512 | <http://metadata-standards.org/11179/> | 404 | <https://www.metadata-standards.org/11179/> |
| 515 | <http://lists.w3.org/Archives/Public/www-tag/2005Jun/0039.html> | 200 | <https://lists.w3.org/Archives/Public/www-tag/2005Jun/0039.html> |
| 517 | <http://www.pc.gov.au/inquiries/completed/data-access> | 200 | <https://www.pc.gov.au/inquiries-and-research/data-access/> |
| 519 | <http://epimorphics.com/public/vocabulary/Registry.html> | 200 | <http://epimorphics.com/public/vocabulary/Registry.html> |
| 521 | <http://www.w3.org/DesignIssues/LinkedData.html> | 200 | <https://www.w3.org/DesignIssues/LinkedData.html> |
| 523 | <http://www.w3.org/TR/coolIRIs/> | 404 | <https://www.w3.org/TR/coolIRIs/> |
| 525 | <http://www.w3.org/2011/gld/wiki/223_Best_Practices_IRI_Construction> | 404 | <https://www.w3.org/2011/gld/wiki/223_Best_Practices_IRI_Construction> |
| 527 | <http://www.w3.org/TR/rdf11-concepts/> | 200 | <https://www.w3.org/TR/rdf11-concepts/> |
| 529 | <http://www.w3.org/TR/rdf-schema/> | 200 | <https://www.w3.org/TR/rdf-schema/> |
| 531 | <https://www.w3.org/TR/vocab-org/> | 200 | <https://www.w3.org/TR/vocab-org/> |
| 533 | <https://www.w3.org/wiki/HashVsSlash> | 200 | <https://www.w3.org/wiki/HashVsSlash> |
| 535 | <https://www.w3.org/TR/html/> | 200 | <https://html.spec.whatwg.org/multipage/> |
| 537 | <https://www.w3.org/standards/semanticweb/data> | 200 | <https://www.w3.org/standards/> |
| 583 | <http://lode2.linked.data.gov.au> | DNS/error | — |
| 583 | <http://vocabs.ardc.edu.au> | 200 | <https://vocabs.ardc.edu.au/> |
