"""Reassemble the frozen HTML exactly, checking every part and final byte hash."""
from pathlib import Path
import gzip,hashlib,json

ROOT=Path(__file__).resolve().parent
meta=json.loads((ROOT/'snapshot/manifest.json').read_text(encoding='utf-8'))
parts=[]
for item in meta['parts']:
    data=(ROOT/'snapshot'/item['file']).read_bytes()
    assert len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256']
    parts.append(data)
compressed=b''.join(parts)
assert len(compressed)==meta['compressedBytes'] and hashlib.sha256(compressed).hexdigest()==meta['compressedSha256']
html=gzip.decompress(compressed)
assert len(html)==meta['htmlBytes'] and hashlib.sha256(html).hexdigest()==meta['htmlSha256']
assert meta['htmlSha256']=='8294e7e9d86bd670ec3382fb75f06091608bccfd4a0c60ade7a62ec2fe6a1fcb'
output=ROOT/'site';output.mkdir(exist_ok=True)
(output/'index.html').write_bytes(html)
(output/'.nojekyll').write_bytes(b'')
print(f"Verified frozen V8: {len(html)} bytes; SHA-256 {meta['htmlSha256']}")
