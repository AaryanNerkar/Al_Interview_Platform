import sys

with open('d:/Hirebyte Final/fin_on_day/InterviewWebsite/frontend/src/components/Analytics/CandidateReport.tsx', 'r') as f:
    text = f.read()

replacements = [
    ('text-cyan', 'text-gold'),
    ('border-cyan', 'border-gold'),
    ('bg-cyan', 'bg-gold'),
    ('shadow-[0_0_15px_rgba(6,182,212,0.5)]', 'shadow-[0_0_15px_rgba(201,168,76,0.5)]'),
    ('drop-shadow-cyan-glow', 'drop-shadow-gold-glow'),
    ('shadow-cyan-glow', 'shadow-gold-glow'),
    ('text-text-primary', 'text-ivory'),
    ('text-text-secondary', 'text-muted'),
    ('text-text-muted', 'text-muted'),
    ('font-mono', 'font-heading'),
    ('font-display', 'font-heading'),
    ('#06B6D4', '#C9A84C'),
    ('#A855F7', '#E8DCC0'),
    ('#3B82F6', '#D4AF37'),
    ('#10b981', '#FAF9F6'),
    ('rgba(6,182,212,0.3)', 'rgba(201,168,76,0.3)'),
    ('rgba(6,182,212,0.5)', 'rgba(201,168,76,0.5)'),
    ('rgba(6,182,212,0.2)', 'rgba(201,168,76,0.2)'),
    ('rgba(6, 182, 212, 0.15)', 'rgba(201, 168, 76, 0.15)'),
    ('rgba(6, 182, 212, 0.2)', 'rgba(201, 168, 76, 0.2)'),
    ('rgba(6, 182, 212, 0.05)', 'rgba(201, 168, 76, 0.05)'),
    ('rgba(6, 182, 212, 0.5)', 'rgba(201, 168, 76, 0.5)'),
    ('hover:bg-cyan/90', 'hover:bg-gold-light'),
    ('text-purple-400', 'text-ivory'),
    ('rgba(168, 85, 247, 0.4)', 'rgba(250, 249, 246, 0.4)'),
    ('rgba(168,85,247,0.4)', 'rgba(250,249,246,0.4)'),
    ('rgba(168, 85, 247, 0.2)', 'rgba(232, 220, 192, 0.2)'),
    ('rgba(168,85,247,0.3)', 'rgba(232,220,192,0.3)'),
    ('hover:bg-purple-500/20', 'hover:bg-[#E8DCC0]/20'),
    ('bg-purple-500/10', 'bg-[#E8DCC0]/10'),
    ('border-purple-500/30', 'border-[#E8DCC0]/30'),
    ('bg-purple-500/5', 'bg-status-red/5'),
    ('border-purple-500/20', 'border-status-red/20'),
    ('hover:border-purple-500/40', 'hover:border-status-red/40'),
    ('rgba(168, 85, 247, 0.4)', 'rgba(239, 68, 68, 0.4)'),
    ("'Fira Code'", "'Outfit'"),
]

for old, new in replacements:
    text = text.replace(old, new)

with open('d:/Hirebyte Final/fin_on_day/InterviewWebsite/frontend/src/components/Analytics/CandidateReport.tsx', 'w') as f:
    f.write(text)
print('Done!')
