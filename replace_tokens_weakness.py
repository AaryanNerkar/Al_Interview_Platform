import sys

with open('d:/Hirebyte Final/fin_on_day/InterviewWebsite/frontend/src/components/Analytics/WeaknessReport.tsx', 'r') as f:
    text = f.read()

replacements = [
    ('text-cyan', 'text-gold'),
    ('border-cyan', 'border-gold'),
    ('bg-cyan', 'bg-gold'),
    ('drop-shadow-cyan-glow', 'drop-shadow-gold-glow'),
    ('text-purple-400', 'text-[#E8DCC0]'),
    ('bg-purple-400', 'bg-[#E8DCC0]'),
    ('bg-purple-500/5', 'bg-[#E8DCC0]/5'),
    ('border-purple-500/20', 'border-[#E8DCC0]/20'),
    ('text-text-primary', 'text-ivory'),
    ('text-text-muted', 'text-muted'),
    ('text-text-error', 'text-status-red'),
    ('border-text-error', 'border-status-red'),
    ('bg-text-error', 'bg-status-red'),
    ('font-mono', 'font-heading'),
    ('font-display', 'font-heading'),
    ('#06B6D4', '#C9A84C'),
    ('#A855F7', '#E8DCC0'),
    ("var(--color-${variant === 'strong' ? 'cyan' : variant === 'risk' ? 'purple-400' : 'text-error'})", "${variant === 'strong' ? '#C9A84C' : variant === 'risk' ? '#E8DCC0' : '#EF4444'}"),
]

for old, new in replacements:
    text = text.replace(old, new)

with open('d:/Hirebyte Final/fin_on_day/InterviewWebsite/frontend/src/components/Analytics/WeaknessReport.tsx', 'w') as f:
    f.write(text)
print('Done!')
