
document.addEventListener("DOMContentLoaded", () => {
    const addDeviceButton = document.getElementById("add-device");
    const deviceList = document.getElementById("device-list");

    // Fetch historical sensor data and update chart
    async function fetchHistoricalData() {
        try {
            const response = await fetch("/api/sensor/batch?batch_size=10");
            if (response.ok) {
                const data = await response.json();
                updateHistoricalChart(data.data);
            } else {
                console.error("Failed to fetch historical data:", response.statusText);
            }
        } catch (error) {
            console.error("Error fetching historical data:", error);
        }
    }

    // Update chart with historical data
    function updateHistoricalChart(sensorBatch) {
        const labels = sensorBatch.map((_, index) => `Record ${index + 1}`);
        const temperatureValues = sensorBatch.map(record => record.temperature);
        const humidityValues = sensorBatch.map(record => record.humidity);

        const ctx = document.getElementById("data-chart").getContext("2d");
        new Chart(ctx, {
            type: "line",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: "Temperature",
                        data: temperatureValues,
                        borderColor: "rgb(255, 99, 132)",
                        tension: 0.1,
                        fill: false
                    },
                    {
                        label: "Humidity",
                        data: humidityValues,
                        borderColor: "rgb(54, 162, 235)",
                        tension: 0.1,
                        fill: false
                    }
                ]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    addDeviceButton.addEventListener("click", () => {
        const deviceName = prompt("Enter device name:");
        if (deviceName) {
            const deviceItem = document.createElement("div");
            deviceItem.textContent = deviceName;
            deviceList.appendChild(deviceItem);
        }
    });

    // Fetch and display historical data on page load
    fetchHistoricalData();
});
