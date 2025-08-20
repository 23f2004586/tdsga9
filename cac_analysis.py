# Email for verification: 23f2004586@ds.study.iitm.ac.in

import matplotlib.pyplot as plt
# Quarterly CAC data (2024)
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
cac_values = [227.47, 229.35, 228.76, 235.05]
average_cac = sum(cac_values) / len(cac_values)
industry_target = 150

# Plot CAC Trend
plt.figure(figsize=(9,6))
plt.plot(quarters, cac_values, marker='o', linestyle='-', label='Quarterly CAC')
plt.axhline(y=industry_target, color='r', linestyle='--', label='Industry Target (150)')
plt.title('Customer Acquisition Cost (CAC) Trend - 2024')
plt.xlabel('Quarter')
plt.ylabel('CAC Value')
plt.ylim(140, 250)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('cac_trend.png')
plt.show()

print(f'Average CAC for 2024: {average_cac:.2f}')
