<h1>SMART FARM</h1>

### Hackathon Material
Welcome to SMART FARM - your comprehensive web application designed to revolutionize farm management. Our platform is tailored to support agronomists, prospective investors, and large plantation owners by providing vital information necessary for maintaining farm health and maximizing productivity.

### Description
Our web application allows agronomists or large plantation owners to monitor their fields using CO2, Temperature and Light sensors. The data gathered from the sensors will be fed to the AI Model so it can generate a report accordingly. If the AI Model detects that the environment in the closed farm has been pretty unhealthy recently, it will suggest that you scan the plants because there is a possibility that the plants are in the early stages of some disease due to the bad environment. Our app offers the option to scan plants and generate a report about the plant's disease and recommendations on how to further prevent the spreading of the disease. The image scanning is done using CNN Algorithm and a model trained on a large dataset. 

## Key Features

### Environmental Monitoring

Our platform offers real-time monitoring of crucial environmental factors within closed farm environments:

- **Temperature**: Stay informed with real-time temperature data, ensuring optimal conditions for plant growth.
- **CO2 Levels**: Continuous monitoring of CO2 levels to guarantee the ideal environment for robust plant growth.
- **Light Intensity**: Accurate measurement and tracking of light intensity to ensure plants receive the necessary light for photosynthesis.

### Plant Health Diagnostics

Detecting and addressing plant diseases promptly is crucial for maintaining farm productivity. Our platform offers:

- **Disease Detection**: Utilizing cutting-edge diagnostic tools, we identify and report any diseases affecting your plants. Our system leverages visual, environmental, and sensor data for comprehensive disease detection.

### Preventive Recommendations

Prevention is key to minimizing plant loss and maximizing yield. SMART FARM provides:

- **Actionable Guidance**: Receive personalized recommendations and best practices tailored to your farm's unique needs. Our platform empowers you with actionable insights to prevent plant loss and optimize productivity.

## How to Use
<h3>Running the Example</h3>

<h4>Preparation</h4>
<ul>
  <li>Start by installing Python and Pip.</li>
  <li><strong>Windows specific</strong>: On Windows, you'll also need to install Visual Studio build tools with CMAKE support (refer to the picture) to run the local Llama model.</li>
</ul>

<h4>Virtual Environment</h4>
<p>It's recommended to set up all requirements in a virtual environment as described <a href="link">here</a>.</p>

<h4>Package Installation</h4>
<p>Install the required Python packages:</p>
<pre><code>pip install llama-cpp-python
pip install HomeAssistant-API
pip install ipympl
pip install tensorflow
pip install opencv-python
pip install Pillow
</code></pre>

<h4>Accessing Home Assistant Instance</h4>
<p>* If you want to change the sensors you can use Home Assistant</p>
<p>API token for accessing our Home Assistant instance:</p>
<pre><code>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIzMGY5NTZmYWQxMTM0YzJiYWVkMmNmMDgxMTk2NmUyNSIsImlhdCI6MTcxNzI0MzA0MywiZXhwIjoyMDMyNjAzMDQzfQ.IOfRnnqDmJ3bA3LYg_sTUGdWFs5djNIIsOPEvSn9ZiE
</code></pre>
<p>Credentials for accessing the Home Assistant dashboard:</p>
<ul>
  <li><strong>Link</strong>: <a href="http://10.11.22.52:8123">http://10.11.22.52:8123</a></li>
  <li><strong>User</strong>: user</li>
  <li><strong>Password</strong>: user</li>
  <p>Act responsibly and fairly - refrain from intentionally damaging anything!</p>
</ul>

<h4>Running the Example</h4>
<p>After you have created the virtual environment, you can type the following command in the terminal:</p>
<pre><code>python app.py
</code></pre>

<h3>Useful Links</h3>
<ul>
  <li><a href="link">MicroPython docs</a></li>
  <li><a href="link">MicroPython sensor node code</a></li>
  <li><a href="link">Home Assistant Docker</a></li>
  <li><a href="link">Raspberry Pi Docker Setup</a></li>
  <li><a href="link">PSoC6 microcontroller board</a></li>
  <li><a href="link">CO2 sensor</a></li>
  <li><a href="link">DPS pressure sensor</a></li>
  <li><a href="link">Radar sensor</a></li>
  <li><a href="link">Stereo Microphone</a></li>
</ul>
<h6>For any additional questions, please feel free to ask us via e-mail gentinuhiu5@gmail.com</h6>
