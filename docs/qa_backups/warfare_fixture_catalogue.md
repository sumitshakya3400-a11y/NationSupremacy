# Warfare acceptance fixture catalogue

This file is **generated** by `verify_warfare_workflows.py --emit-catalogue`.
It is a projection of `warfare_fixture_registry.json`, which is the single
canonical machine-readable mapping between documented fixtures and the
executable functions in the validator. A fixture that appears here but has
no callable implementation, an executor whose source hash differs, a
mutation that does not produce the declared target value, or an executable
fixture absent here fails check 47.

| Fixture | Name | Exact mutation | Expected check | Expected reason | Executable | Result |
|---|---|---|---|---|---|---|
| PF-01 | header and design-only status | none — the unmutated document is run | 01 | clean document satisfies this check | check_01 | Accepted |
| PF-02 | fixed constraints unchanged | none — the unmutated document is run | 02 | clean document satisfies this check | check_02 | Accepted |
| PF-03 | nine-operation catalogue | none — the unmutated document is run | 03 | clean document satisfies this check | check_03 | Accepted |
| PF-04 | workflow schema complete | none — the unmutated document is run | 06 | clean document satisfies this check | check_06 | Accepted |
| PF-05 | two-table test schema joins | none — the unmutated document is run | 09 | clean document satisfies this check | check_09 | Accepted |
| PF-06 | failure-code coverage and gaps | none — the unmutated document is run | 27 | clean document satisfies this check | check_27 | Accepted |
| PF-07 | requirement rows complete | none — the unmutated document is run | 21 | clean document satisfies this check | check_21 | Accepted |
| PF-08 | formula inventory from register | none — the unmutated document is run | 24 | clean document satisfies this check | check_24 | Accepted |
| PF-09 | audit-event coverage | none — the unmutated document is run | 26 | clean document satisfies this check | check_26 | Accepted |
| PF-10 | integration contracts complete | none — the unmutated document is run | 30 | clean document satisfies this check | check_30 | Accepted |
| PF-11 | WAR rule inventory exact | none — the unmutated document is run | 31 | clean document satisfies this check | check_31 | Accepted |
| PF-12 | D-014 and owner-reserved consistency | none — the unmutated document is run | 34 | clean document satisfies this check | check_34 | Accepted |
| PF-13 | ten orphan totals at zero | none — the unmutated document is run | 41 | clean document satisfies this check | check_41 | Accepted |
| NF-01 | remove the document version | replace '**Version:** 1.0' with '**Version:**' in doc | 01 | header missing '**Version:** 1.0' | mutation_01 | Rejected |
| NF-02 | weaken a fixed constraint | replace '**Protected decisions preserved.**' with '**Protected decisions noted.**' in doc | 02 | constraint text missing '**Protected decisions preserved.**' | mutation_02 | Rejected |
| NF-03 | add a tenth operation | replace '`OP-09 RESUPPLY`' with '`OP-09 RESUPPLY` `OP-10 ESPIONAGE`' in doc | 03 | operation beyond OP-09 | mutation_03 | Rejected |
| NF-04 | delete lifecycle step 25 | delete row '/ 25 /' | 04 | lifecycle steps must be 1..25 | mutation_04 | Rejected |
| NF-05 | duplicate a workflow heading | replace '#### WFW-002 — Declaration rejected' with '#### WFW-001 — Declaration rejected' in doc | 05 | workflow headings must be WFW-001..040 in order | mutation_05 | Rejected |
| NF-06 | rename a mandatory workflow field | replace '/ Consent / Unilateral' with '/ ConsentX / Unilateral' in doc | 06 | fields differ (found 22 of 23) | mutation_06 | Rejected |
| NF-07 | add an eighteenth journey | replace '**J17 — Loss cap reached mid-campaign.**' with '**J18 — Loss cap reached mid-campaign.**' in doc | 07 | journeys must be J1..J17 | mutation_07 | Rejected |
| NF-08 | renumber an edge case to WFE-061 | replace '/ `WFE-060` /' with '/ `WFE-061` /' in doc | 08 | edge-case IDs are not WFE-001..060 | mutation_08 | Rejected |
| NF-09 | delete a test identification row | delete row '/ `WFA-124` /' | 09 | identification and behaviour sets differ | mutation_09 | Rejected |
| NF-10 | mark a definition INCOMPLETE | edit row '/ `WFA-001` /', field 8: 'COMPLETE' → 'INCOMPLETE' | 10 | Definition is 'INCOMPLETE' | mutation_10 | Rejected |
| NF-11 | use an invalid phase | edit row '/ `WFA-002` /', field 3: 'OPEN' → 'P6' | 11 | invalid phase 'P6' | mutation_11 | Rejected |
| NF-12 | assign a class-P test to class A | edit row '/ `WFA-121` /', field 2: 'P' → 'A' | 12 | class distribution | mutation_13 | Rejected |
| NF-13 | change an edge-case class so it disagrees with its test | edit row '/ `WFE-001` /', field 1: 'A' → 'B' | 13 | class B disagrees with WFA-001 class A | nf13 | Rejected |
| NF-14 | point a test at WFE-999 | edit row '/ `WFA-001` /', field 5: 'WFE-001' → 'WFE-999' | 14 | unknown WFE-999 | mutation_14 | Rejected |
| NF-15 | point a test at WFW-999 | edit row '/ `WFA-001` /', field 4: 'WFW-001, WFW-002' → 'WFW-999' | 15 | unknown WFW-999 | mutation_15 | Rejected |
| NF-16 | point a test at REQ-704 | edit row '/ `WFA-001` /', field 3: 'REQ-654, REQ-678' → 'REQ-704' | 16 | REQ-704 outside REQ-654–REQ-703 | mutation_16 | Rejected |
| NF-17 | cite unallocated WRF-19 | edit row '/ `WFA-001` /', field 6: '`WAR-001`, `WAR-009d`, `WRF-01`' → '`WAR-001`, `WRF-19`' | 17 | cites unallocated WRF-19 | mutation_17 | Rejected |
| NF-18 | cite WAR-189 | edit row '/ `WFA-001` /', field 6: '`WAR-001`, `WAR-009d`, `WRF-01`' → '`WAR-001`, `WAR-189`' | 17 | WAR-189 is not in the B-10 inventory | mutation_18 | Rejected |
| NF-19 | cite WRA-15 | edit row '/ `WFA-001` /', field 6: '`WAR-001`, `WAR-009d`, `WRF-01`' → '`WAR-001`, `WRA-15`' | 17 | unknown WRA-15 | mutation_19 | Rejected |
| NF-20 | cite F-WR-040 | edit row '/ `WFA-001` /', field 6: '`WAR-001`, `WAR-009d`, `WRF-01`' → '`WAR-001`, `F-WR-040`' | 17 | unknown F-WR-040 | nf20 | Rejected |
| NF-21 | point an edge case at WFA-999 | edit row '/ `WFE-001` /', field 5: 'WFA-001' → '`WFA-999`' | 13 | primary test WFA-999 does not exist | mutation_21 | Rejected |
| NF-22 | make an edge case cite a test that does not cite it | edit row '/ `WFE-001` /', field 5: 'WFA-001' → '`WFA-002`' | 19 | primary test WFA-002 does not cite it | mutation_22 | Rejected |
| NF-23 | delete REQ-703 | delete row '/ REQ-703 /' | 21 | requirement rows must be 654..703 | mutation_23 | Rejected |
| NF-24 | point a requirement at WFW-999 | edit row '/ REQ-654 /', field 3: 'WFW-001, 004, 027, 040' → '`WFW-999`' | 23 | REQ-654: unknown WFW-999 | mutation_24 | Rejected |
| NF-25 | point a requirement at WFA-999 | edit row '/ REQ-655 /', field 4: 'WFA-046, WFA-083, WFA-084' → '`WFA-999`' | 23 | REQ-655: unknown WFA-999 | mutation_25 | Rejected |
| NF-26 | delete F-WR-039 | delete row '/ `F-WR-039` /' | 24 | formula rows must be 001..039 | mutation_26 | Rejected |
| NF-27 | point a formula at WFW-999 | edit row '/ `F-WR-001` /', field 2: 'WFW-027' → '`WFW-999`' | 25 | F-WR-001: unknown WFW-999 | mutation_27 | Rejected |
| NF-28 | point a formula at WFA-999 | edit row '/ `F-WR-001` /', field 3: 'WFA-039, WFA-040' → '`WFA-999`' | 25 | F-WR-001: unknown WFA-999 | mutation_28 | Rejected |
| NF-29 | delete WRA-14 | delete row '/ `WRA-14` ' | 26 | expected 14 audit rows, found 13 | mutation_29 | Rejected |
| NF-30 | redefine WRF-14 as the gap WRF-15 | replace '/ `WRF-14` /' with '/ `WRF-15` /' in doc | 27 | defined WRF codes differ from the 32-code set | mutation_30 | Rejected |
| NF-31 | delete B10-AD-25 | delete row '/ `B10-AD-25` /' | 28 | B10-AD rows must be 01..25 | mutation_31 | Rejected |
| NF-32 | delete B10-C34 | delete row '/ `B10-C34` /' | 29 | B10-C rows must be 01..34 | mutation_32 | Rejected |
| NF-33 | delete an integration row | delete row '/ 13 / Prompt 15 /' | 30 | expected 13 integration rows, found 12 | mutation_33 | Rejected |
| NF-34 | blank an integration contract field | edit row '/ 13 /', field 7: 'none — documentation' → '' | 30 | empty mutation owner | mutation_34 | Rejected |
| NF-35 | point an integration test at WFA-999 | edit row '/ 1 /', field 5: 'WFA-112' → '`WFA-999`' | 30 | unknown WFA-999 | nf35 | Rejected |
| NF-36 | shorten a WAR range | replace '`WAR-183`–`WAR-188`' with '`WAR-183`–`WAR-187`' in doc | 31 | WAR ranges are incomplete or overlapping | mutation_36 | Rejected |
| NF-37 | delete a lettered sub-rule | delete row '/ `WAR-163b` /' | 32 | lettered table has 41 rows, expected 42 | mutation_37 | Rejected |
| NF-38 | mark a UD-040 owner decision resolved | replace '/ `UD-040` / Open /' with '/ `UD-040` / Resolved /' in unresolved | 34 | UD-040 status is 'Resolved', expected Open | mutation_38 | Rejected |
| NF-39 | claim a runtime pass | append 'This suite was runtime-passed.' to doc | 36 | positive runtime claim | mutation_36r | Rejected |
| NF-40 | introduce a mapless violation | append 'A province_id is used for supply.' to doc | 37 | forbidden construct present: 'province_id' | mutation_37f | Rejected |
| NF-41 | point a numbered-WAR range workflow at WFW-999 | edit row '/ `WAR-001`–`WAR-014` /', field 2: 'WFW-001, 002, 018' → '`WFW-999`' | 44 | range 001–014: invalid or empty workflow mapping | c41 | Rejected |
| NF-42 | point a numbered-WAR range acceptance test at WFA-999 | edit row '/ `WAR-001`–`WAR-014` /', field 3: 'WFA-001, 016, 097, 098' → '`WFA-999`' | 44 | range 001–014: invalid or empty test mapping | c42 | Rejected |
| NF-43 | point a lettered-WAR row workflow at WFW-999 | edit row '/ `WAR-005a` /', field 2: 'WFW-001' → '`WFW-999`' | 44 | invalid workflow WFW-999 | c43 | Rejected |
| NF-44 | point a lettered-WAR row test at WFA-999 | edit row '/ `WAR-005a` /', field 3: 'WFA-008' → '`WFA-999`' | 44 | nonexistent test WFA-999 | c44 | Rejected |
| NF-45 | insert WAR-999 into a numbered range | replace '/ `WAR-001`–`WAR-014` /' with '/ `WAR-001`–`WAR-014`, `WAR-999` /' in doc | 44 | WAR ranges do not equal B-10 numbered definitions | c45 | Rejected |
| NF-46 | insert a fabricated lettered rule | insert line '/ `WAR-005z` / Fabricated sub-rule / WFW-001 / WFA-001 /' | 44 | lettered table differs from B-10 | c46 | Rejected |
| NF-47 | cite an invalid formula from a test | replace '/ `F-WR-006` / COMPLETE /' with '/ `F-WR-040` / COMPLETE /' in doc | 44 | test WFA-004 names unknown F-WR-040 | c47 | Rejected |
| NF-48 | claim a DIRECT disposition without a citing test | replace '/ Numbered `WAR-001`–`WAR-188` / 188 / 95 /' with '/ Numbered `WAR-001`–`WAR-188` / 188 / 96 /' in doc | 44 | != derived [188, 95, 93, 0, 0] | c48 | Rejected |
| NF-49 | remove the workflow source mapping from a WFA record | edit row '/ `WFA-003` /', field 4: 'WFW-020, WFW-040' → '' | 15 | no workflow reference | c49 | Rejected |
| NF-50 | orphan WFW-040 | replace 'WFW-040' with 'WFW-039' in doc within lines containing '/ `WFA-' | 18 | no dedicated test outside the end-to-end scenario | c50 | Rejected |
| NF-51 | orphan WFE-060 | edit row '/ `WFE-060` /', field 5: 'WFA-116' → '`WFA-001`' | 19 | primary test WFA-001 does not cite it | c51 | Rejected |
| NF-52 | orphan WFA-124 | delete row '/ `WFA-124` /' | 09 | expected 124 identification rows, found 123 | c52 | Rejected |
| NF-53 | point a B-02 integration source at B-99 / FAKE-999 | edit row '/ 1 / B-02 phases /', field 2: 'B-02 `TR-040`, `TR-050`, `TR-059`' → 'B-99 / `FAKE-999`' | 45 | source identifier FAKE-999 does not exist in b02 | c53 | Rejected |
| NF-54 | cite a nonexistent B-03 protection rule | edit row '/ 2 / B-03 protection', field 2: '`ACC-016`, `NET-015`; `ONB-019`, `ONB-023`, `ONB-037`, `ONB-039`' → '`ACC-016`, `NET-015`; `ONB-019`, `ONB-023`, `ONB-037`, `ONB-039`, `ONB-999`' | 45 | source identifier ONB-999 does not exist in b03 | c54 | Rejected |
| NF-55 | cite a nonexistent B-04 Food rule | edit row '/ 3 / B-04 economy', field 2: '`ECN-105`, `ECN-119`, `ECN-152`, `ECN-163`, `ECN-214`' → '`ECN-105`, `ECN-119`, `ECN-152`, `ECN-163`, `ECN-214`, `ECN-999`' | 45 | source identifier ECN-999 does not exist in b04 | c55 | Rejected |
| NF-56 | cite a nonexistent B-05 infrastructure rule | edit row '/ 4 / B-05 cities', field 2: '`URB-042`, `URB-046`, `URB-051a`, `URB-118a`, `URB-118b`' → '`URB-042`, `URB-046`, `URB-051a`, `URB-118a`, `URB-118b`, `URB-999`' | 45 | source identifier URB-999 does not exist in b05 | c56 | Rejected |
| NF-57 | cite a nonexistent B-06 political rule | edit row '/ 5 / B-06 population', field 2: '`DMP-030`, `DMP-031`, `DMP-031a`, `DMP-045`, `DMP-052`' → '`DMP-030`, `DMP-031`, `DMP-031a`, `DMP-045`, `DMP-052`, `DMP-999`' | 45 | source identifier DMP-999 does not exist in b06 | c57 | Rejected |
| NF-58 | cite a nonexistent B-07 trade rule | edit row '/ 6 / B-07 market', field 2: 'B-07 `MKT-009`, `MKT-218`' → 'B-07 `MKT-009`, `MKT-218`, `MKT-999`' | 45 | source identifier MKT-999 does not exist in b07 | c58 | Rejected |
| NF-59 | cite a nonexistent B-08 diplomatic rule | edit row '/ 7 / B-08 diplomacy', field 2: '`DIP-037`, `DIP-070`, `DIP-141`' → '`DIP-037`, `DIP-070`, `DIP-141`, `DIP-999`' | 45 | source identifier DIP-999 does not exist in b08 | c59 | Rejected |
| NF-60 | cite a nonexistent B-09 Alliance rule | edit row '/ 8 / B-09 Alliance', field 2: '`ALL-199`, `ALL-204`, `ALL-206`, `ALL-208`, `AUD-AL-017`, `AT-E01`' → '`ALL-199`, `ALL-204`, `ALL-206`, `ALL-208`, `AUD-AL-017`, `AT-E01`, `ALL-999`' | 45 | source identifier ALL-999 does not exist in b09 | c60 | Rejected |
| NF-61 | point an integration workflow at WFW-999 | edit row '/ 1 / B-02 phases /', field 3: 'WFW-001, 027, 040' → 'WFW-999' | 45 | unknown WFW-999 | c61 | Rejected |
| NF-62 | point an integration test at WFA-999 | edit row '/ 1 / B-02 phases /', field 5: 'WFA-112' → 'WFA-999' | 45 | unknown WFA-999 | c62 | Rejected |
| NF-63 | remove an integration validation owner | edit row '/ 1 / B-02 phases /', field 6: 'B-10 P3.7/P5 scheduler' → '' | 45 | validation owner invalid (empty mandatory field) | c63 | Rejected |
| NF-64 | remove an integration mutation owner | edit row '/ 1 / B-02 phases /', field 7: 'B-02 phase engine' → '' | 45 | mutation owner invalid (empty mandatory field) | c64 | Rejected |
| NF-65 | remove integration phase ordering | edit row '/ 1 / B-02 phases /', field 9: '`WAR-040` single-flight; P3.7 precedes P5' → '' | 45 | ordering invalid (empty mandatory field) | c65 | Rejected |
| NF-66 | remove integration failure handling | edit row '/ 1 / B-02 phases /', field 11: '`WRF-34`; resume from the last committed checkpoint' → '' | 45 | failure/recovery invalid (empty mandatory field) | c66 | Rejected |
| NF-67 | remove integration privacy | edit row '/ 1 / B-02 phases /', field 13: 'moderators; actors see their own records' → '' | 45 | privacy invalid (empty mandatory field) | c67 | Rejected |
| NA-01 | bare N/A formula | set a mandatory cell to 'N/A' | NA | bare N/A formula | justified_value | Rejected |
| NA-02 | bare N/A ledger | set a mandatory cell to 'N/A' | NA | bare N/A ledger | justified_value | Rejected |
| NA-03 | bare NONE audit | set a mandatory cell to 'NONE' | NA | bare NONE audit | justified_value | Rejected |
| NA-04 | bare none failure | set a mandatory cell to 'none' | NA | bare none failure | justified_value | Rejected |
| NA-05 | empty mandatory field | set a mandatory cell to '' | NA | empty mandatory field | justified_value | Rejected |
| NA-06 | empty N/A reason | set a mandatory cell to 'N/A — ' | NA | empty N/A reason | justified_value | Rejected |
| NA-07 | punctuation-only justification | set a mandatory cell to 'N/A — ...' | NA | punctuation-only justification | justified_value | Rejected |
| NA-08 | valid N/A with a meaningful explanation | set a mandatory cell to 'N/A — no failure code exists for a lawful outcome' | NA | valid N/A with a meaningful explanation | justified_value | Accepted |
| NA-09 | valid NONE with a meaningful explanation | set a mandatory cell to 'none — a read-only query writes no ledger item' | NA | valid NONE with a meaningful explanation | justified_value | Accepted |
| NA-10 | valid existing formula identifier | set a mandatory cell to '`F-WR-031`' | NA | valid existing formula identifier | justified_value | Accepted |

Totals: 13 positive, 67 negative, 10 N/A.
