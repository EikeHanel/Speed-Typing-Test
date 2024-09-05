<h1 align="center">Typing Speed Test</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Project Status">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Tkinter-GUI-yellow" alt="Tkinter GUI">
</p>

<p align="center">
  A simple typing speed test application built using Python's Tkinter library. It generates random words, measures your typing speed in words per minute (WPM), and highlights keystrokes based on correctness.
</p>

<h2>Features</h2>
<ul>
  <li>Generates a new set of random words every time the test starts.</li>
  <li>Real-time keystroke validation with visual feedback (correct keystrokes in green, incorrect in red).</li>
  <li>One-minute timer to evaluate typing speed.</li>
  <li>Displays words per minute (WPM) after the timer ends.</li>
  <li>Option to restart the test after completion.</li>
</ul>

<h2>Installation</h2>
<p>Ensure you have Python installed (version 3.9 or later). Follow the steps below:</p>

<ol>
  <li>Clone this repository:</li>
  <pre><code>git clone https://github.com/your-username/typing-speed-test.git</code></pre>
  <li>Navigate to the project folder:</li>
  <pre><code>cd typing-speed-test</code></pre>
  <li>Ensure you have the required dependencies (Tkinter is included with Python by default):</li>
  <pre><code>pip install tk</code></pre>
  <li>Run the program:</li>
  <pre><code>python main.py</code></pre>
</ol>

<h2>Usage</h2>
<p>Once the program starts, a set of 30 random words will appear on the screen. You have 60 seconds to type as many words correctly as you can. The test will automatically evaluate each word you type and give you visual feedback:</p>
<ul>
  <li>Green for correct keystrokes.</li>
  <li>Red for incorrect keystrokes.</li>
</ul>
<p>After the time runs out, your words per minute (WPM) score will be displayed, and you can restart the test by clicking the "Restart" button.</p>

<h2>Project Structure</h2>
<ul>
  <li><code>main.py</code> - The main entry point for starting the program.</li>
  <li><code>speed_typing_test.py</code> - Contains the main logic for the typing test and user interface.</li>
  <li><code>word_list.py</code> - Contains a list of common words used for generating the random words during the test.</li>
</ul>

<h2>Customization</h2>
<p>You can customize the behavior of the program by modifying the following constants in <code>speed_typing_test.py</code>:</p>
<ul>
  <li><strong>THEME_COLOR:</strong> Change the background color of the window.</li>
  <li><strong>BG, FG:</strong> Customize the background and foreground colors for the text display and entry fields.</li>
  <li><strong>FONT:</strong> Modify the font family and size used in the application.</li>
  <li><strong>TIMER_TIME:</strong> Adjust the duration of the typing test (default is 60 seconds).</li>
</ul>

<h2>Screenshots</h2>
<p align="center">
  <img src="/speedtypingtest.png" alt="Typing Test Screenshot" width="500">
</p>

<h2>Contributing</h2>
<p>Feel free to fork this repository and submit pull requests for any improvements or bug fixes!</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>

