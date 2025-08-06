🖇 Prerequisites
----------------

*   Python 3.8 or newer
    
*   pip
    

🚀 Installation
---------------

1.  git clone https://github.com/your-user/yt-transcript-scraper.gitcd yt-transcript-scraper
    
2.  pip install -r requirements.txt**requirements.txt**shellCopyEditpytube>=15.0youtube-transcript-api>=0.6
    

🏃 Usage
--------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   youtube_scraper.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"   `

*   Outputs a JSON file (e.g., dQw4w9WgXcQ.json) in the current directory.
    
*   The script will print the absolute path of the saved file.
    

📝 Example Output
-----------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",    "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",    "transcript": "We're no strangers to love ..."  }   `

🔄 Using With Gemini
--------------------

Once the script produces your JSON file, upload it to Gemini and prompt:

> Summarize the video in depth, preserving all details, steps, workflows, and how-tos from the transcript.

The tool ensures Gemini has everything needed for a comprehensive and context-rich summary.

⚙️ Customization & Extending
----------------------------

*   **Multiple URLs:** Wrap the script logic in a loop or accept a file with URLs.
    
*   **Other languages:** Edit the languages=\[...\] parameter in the code.
    
*   **Bulk or automated use:** Add delays, proxies, or error handling as needed.
    
*   **Other output formats:** Save .srt or push results to a database.
    

🛠 Troubleshooting
------------------

SymptomLikely CauseSolutionTranscript unavailable / placeholderCaptions are disabledNone; script will note this"Could not find match" errorInvalid or private URLCheck video visibility

🤝 Contributing
---------------

Pull requests are welcome!

1.  Fork this repo
    
2.  Create a feature branch
    
3.  Commit and push your changes
    
4.  Open a pull request 🚀
    

📜 License
----------

This project is licensed under the **Apache License, Version 2.0**.See the [LICENSE](LICENSE) file for full license text.

> © 2025 Your Name. Provided as-is, without warranty.