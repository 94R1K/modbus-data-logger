async function fetchCurrentValue() {
  const response = await fetch('/current_value');
  const data = await response.json();
  document.getElementById('current-value').innerText = data.value;
}

async function fetchGraphData() {
  const response = await fetch('/last_hour_data');
  const graphHtml = await response.text();
  document.getElementById('graph').innerHTML = graphHtml;
}

setInterval(fetchCurrentValue, 1000);
setInterval(fetchGraphData, 60000);

await fetchCurrentValue();
await fetchGraphData();