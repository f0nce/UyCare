from pathlib import Path
import json,re,xml.etree.ElementTree as ET
r=Path(__file__).resolve().parents[1]
required=['README.md','CONTRIBUTING.md','.gitignore','.env.example','docs/01-project-proposal.md','docs/02-relevance-and-discovery.md','docs/03-literature-review.md','docs/04-existing-system-comparison.md','docs/05-technology-comparison.md','docs/06-requirements.md','docs/07-architecture.md','docs/08-ux-and-prototype.md','docs/09-verification-and-evaluation.md','docs/10-project-management.md','docs/11-supervisor-feedback.md','docs/12-references.md','docs/traceability.md','prototype/index.html','prototype/app.js','prototype/styles.css','management/youtrack-backlog.csv','tests/acceptance-cases.md','submission/checklist.md']
for x in required:assert (r/x).is_file() and (r/x).stat().st_size>0,x
refs=json.loads((r/'docs/sources.json').read_text());published=[x for x in refs if x['type'] in ['Journal article','Conference paper','Workshop paper']]
assert len(refs)>=12 and len(published)>=8
req=json.loads((r/'docs/requirements.json').read_text());allreq=req['functional']+req['nonfunctional'];ids=[x['id'] for x in allreq];assert len(ids)==len(set(ids))
trace=(r/'docs/traceability.md').read_text();tests=(r/'tests/acceptance-cases.md').read_text()
for x in allreq:assert x['acceptance'] and x['id'] in trace and x['id'] in tests,x['id']
for name in ['system-context','use-cases','components','job-lifecycle']:
 for ext in ['svg','drawio']:ET.parse(r/'diagrams'/f'{name}.{ext}')
for p in r.rglob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if not re.match(r'https?://|#',target):assert (p.parent/target.split('#')[0]).exists(),f'{p}: {target}'
print(f'Package checks passed: {len(required)} required files, {len(refs)} sources, {len(published)} published scientific works, {len(allreq)} traceable requirements, 4 diagram pairs.')
print('These checks do not validate interviews, supervisor approval, live YouTrack, individual contributions or production implementation.')
