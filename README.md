<h1>Make Your Smart Home Smarter with Infineon Sensors and Generative AI</h1>

<h2>Submission Details</h2>

<h3>Hackathon Material</h3>
<ul>
  <li><strong>Topic Introduction Slides (Friday)</strong></li>
  <li><strong>Challenge Introduction Slides (Saturday)</strong></li>
</ul>

<h3>Running the Example</h3>

<h4>Overview</h4>
<p>The example serves as a reference to kickstart your journey with our topic. You're not obliged to run the example or adhere to the same approach. Feel free to utilize GenAI APIs instead of the local Llama model used in the example.</p>

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
pip install notebook
pip install ipympl # (for plotting)
</code></pre>

<h4>Cloning this Repository</h4>
<p>Clone this git repo:</p>
<pre><code>git clone https://github.com/Infineon/hackathon
cd hackathon/examples
</code></pre>

<h4>Accessing Home Assistant Instance</h4>
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
<p>Download the LLAMA model and type the following command to run the example:</p>
<pre><code>jupyter notebook llama_example.ipynb
</code></pre>
<p>Note: This example serves as a basic workflow demonstration and might output incomplete results. Your task is to enhance it!</p>

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

<h3>Infineon Team</h3>
<ul>
  <li><strong>Eric</strong> (Embedded Systems Engineer)</li>
  <li><strong>Julian</strong> (Staff Embedded Systems Engineer)</li>
</ul>

<h4>How to Reach Us?</h4>
<p>Open an issue in this repository or connect with us onsite.</p>
