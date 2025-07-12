// This file is loaded only if included from HTML
// Requires `timestamps` and `short_code` to be globally available

if (typeof timestamps !== "undefined") {
  const counts = {};

  timestamps.forEach(t => {
    const date = new Date(t).toISOString().split("T")[0];
    counts[date] = (counts[date] || 0) + 1;
  });

  const labels = Object.keys(counts);
  const data = Object.values(counts);

  new Chart(document.getElementById("chart"), {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Visits per Day',
        data: data,
        backgroundColor: '#0070f3'
      }]
    },
    options: {
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
}