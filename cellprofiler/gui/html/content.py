startup_main = '''<html>
<body>
<center><h2>Welcome to CellProfiler!</h2></center>
<p>CellProfiler is automated image analysis software designed to measure biological phenotypes in images.</p>
<br>
<br>
From here, you can...
<table border="0" cellpadding="5" width="100%">
<tr>
    <td width="200"><i>Get oriented</i></td>
    <td>See this <a href="startup_interface">summary</a> for a quick overview of CellProfiler's interface.</td>
</tr>
<tr>
    <td width="200"><i>Read the documentation</i></td>
    <td>There is an <a href="http://cellprofiler.org/manual">online manual</a>. Also, detailed help is available for any module by clicking the "<b>?</b>" button, or using the <i>Help</i> menu in the toolbar.</td>
 </tr>
<tr>
    <td><i>Try example pipelines</i></td>
    <td>The <a href="http://www.cellprofiler.org/examples.htm">Examples</a> page on our website has pipelines and images of various biological assays. You can pick one that most resemble your phenotypes of interest and begin adjusting its settings.</td>
</tr>
<tr>
    <td><i>Watch our tutorials</i></td>
    <td>Videos of CellProfiler demos are available on the <a href="http://www.cellprofiler.org/tutorials.htm">Tutorials</a> page.</td>
</tr>
<tr>
    <td><i>Get user support</i></td>
    <td>If you need help or advice, you can post a question in our online <a href="http://www.cellprofiler.org/forum/">forum.</a></td>
</tr>
</table>
<p>Click <a href="pref:no_display">here</a> to stop displaying this page when CellProfiler starts.</p>
</body>
</html>'''

startup_interface = '''<html>
<body>
<h2>Summary of the Interface</h2>
The CellProfiler interface has tools for managing images, pipelines and modules. The interface is divided into four main parts, as shown in the following illustration:
<p>
<center>
<img src="memory:cp_panel_schematic.png"></img>
</center>
<p>
<table cellspacing="0" class="body" cellpadding="4" border="2">
<colgroup><col width="200"><col width="300%"></colgroup>
<thead><tr valign="top"><th bgcolor="#B2B2B2">Element</th><th bgcolor="#B2B2B2">Description</th></tr></thead>
<tbody>
<tr><td><i>Pipeline</i></td><td>Lists the modules in the pipeline, with controls for display and testing. Below this panel are tools for adding, removing, and reordering modules and getting help.</td></tr>
<tr><td><i>Files</i></td><td>Lists images and pipeline files in the current input folder.</td></tr>
<tr><td><i>Module Settings</i></td><td>Contains the options for the currently selected module.</td></tr>
<tr><td><i>Folders</i></td><td>Dialogs for controlling default input and output folders and output filename.</td></tr>
</tbody></table>
<p>Go <a href="startup_main">back</a> to the main startup page.</p>
</body>
</html>'''

def find_link(name):
    return globals().get(name, None)
