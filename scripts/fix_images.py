from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'index.html'
s = p.read_text(encoding='utf-8')
replacements = {
    'href="image.png"': 'href="/process_pictures/p1/image.png"',
    'src="image.png"': 'src="/process_pictures/p1/image.png"',
    'href="1000055280.jpg"': 'href="/process_pictures/p1/ExportBlock-baf7cf85-6b73-495c-a5e0-f6f3b05d0616-Part-1/1000055280.jpg"',
    'src="1000055280.jpg"': 'src="/process_pictures/p1/ExportBlock-baf7cf85-6b73-495c-a5e0-f6f3b05d0616-Part-1/1000055280.jpg"',
}
for k,v in replacements.items():
    s = s.replace(k, v)
p.write_text(s, encoding='utf-8')
print('done')
