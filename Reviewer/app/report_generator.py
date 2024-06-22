
import os
import shutil

REPORT_TITLE = "tS Ревью миссии"
REPORT_HEADER = 'Ревью миссии'
REPORT_LINK = 'https://tacticalshift.github.io'

HTML_FAVICON_BASE64 = '<link rel="shortcut icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABoElEQVRYhe3XMUhVURzH8c/L94bekGZU4JCVL2swHDKIlqAlEcrFiIJA2opwCCScbWhqaIgopCLCoGiJloZcLLCwKCgqH+VQBtKr0HpllrfhKiJIpPfFvcL7LYdz+HN+P76H8z+c1P26pkCMWhaneTkApIIgCGDkci8YPnVm/sqKCrDuxFGwtm0fyKxaGSlA7ATS/1q4/mQHqDlyCIwNPgWFu32RAiwdAmva9oIv/QPgRfvxkgRIDoGa9oNzxhk9yG2fMw+mpkoaIDkEvr3Kg/HHz+YtHL15G7O3oKH3Aijm3/7dIWwzJj8Wwn1u3QET70aQAAKL74T7W0GmumpBhr/Gv4Lnh49hSRGIqOyWTaDh2nlQHHqDBBBI//7+A2SqKv+rUfHlEGbfjtWtLUgCgbGHg6B6z26QvXgVFKf7QqmV3ZwDk4VPSACB1JPmAwFsvdETrqTD+/75Xj943dEFNnZ3RTLK1teBFdsawfDps0gCgZl/wfLcBlDbGb7zlTuawEDjLrAz/yiS0c/pM/9w5Tp4f+4SkkQgLsVOoBygHOAP/YZ+YJu5QhUAAAAASUVORK5CYII=" />'

HTML_PAGE = """
<!DOCTYPE html>
<html lang="us">
    {head}
    {body}
</html>
"""
HTML_HEAD = """
    <head>
        <meta charset="utf-8"/>
        <title>{title}</title>

        {favicon}
        <link rel="stylesheet" href="src/style.css">
        <link rel="stylesheet" href="src/languages/styles/atom-one-light.min.css">

        <script src="https://code.jquery.com/jquery-3.4.1.min.js"
        integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
        crossorigin="anonymous"></script>
        <script src="src/highlight.min.js"></script>
        <script src="src/languages/cpp.min.js"></script>
        <script src="src/languages/sqf.min.js"></script>
        <script src="src/languages/yaml.min.js"></script>
        <script src="src/highlight-line-numbers.min.js"></script>

        <script src="src/data.js"></script>
        <script src="src/app.js"></script>
    </head>
"""
HTML_BODY = """
    <body>
        <div id="header">
            <div id="header-title">
                <span>
                    <a href="{report_home_link}" style="text-decoration: none; color: inherit;">tS</a></span>
                    <tt id='header-sans'>{report_header}</tt> - <span id="header-mission-name" style="font-family: system-ui"></span>
                    <tt id="header-current-page" style="font-family: system-ui;font-size:21px;"></tt>
                <button id="header-btn-up" title="Вернуться наверх">Наверх!</button>
            </div>
        </div>

        <div id="navbar">
            <ul></ul>
        </div>

        <div id="wrapper">
            <div id="info">
                <h3>Информация</h3>
                <div></div>
            </div>
            <div id="raw-content">
                <h3>Содержимое</h3>
                <div></div>
            </div>

            <div id="footer"></div>
        </div>
    </body>
"""


class ReportGenerator:
    """Creates HTML report
    """

    SRC_DIR = "src"
    REPORT_HTML = "Report.html"
    DATA_JS = "data.js"
    DATA_JS_PREFIX = 'const MissionReviewData = '

    def __init__(self, mission_name, mission_creation_date):
        self.app_dir = os.path.split(os.path.dirname(__file__))[0]
        self.report_dir = "_".join([
            "Report",
            mission_name,
            mission_creation_date
        ]).replace(":", "-")
        self.report_src_dir = os.path.join(self.report_dir, self.SRC_DIR)

    def create_report(self, report_content: str | dict,
                      overview_img_path: str):
        """Creates report directory and files

        Args:
            report_content (str | dict): reprot content
            overview_img_path (str): path to overview image to copy to report
        """
        self._create_report_dir()
        self._create_report_file()
        self._create_data_file(report_content)
        self._copy_overview_img(overview_img_path)

    def _create_report_dir(self):
        if os.path.exists(self.report_dir):
            shutil.rmtree(self.report_dir)

        os.mkdir(self.report_dir)
        src_dir = os.path.join(self.app_dir, self.SRC_DIR)
        shutil.copytree(src_dir, self.report_src_dir)

    def _create_report_file(self):
        head = HTML_HEAD.format(
            title=REPORT_TITLE,
            favicon=HTML_FAVICON_BASE64
        )
        body = HTML_BODY.format(
            report_header=REPORT_HEADER,
            report_home_link=REPORT_LINK
        )
        content = HTML_PAGE.format(
            head=head,
            body=body
        )
        report_file = os.path.join(self.report_dir, self.REPORT_HTML)
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(content)

    def _create_data_file(self, content):
        data_js_filename = os.path.join(self.report_src_dir, self.DATA_JS)
        with open(data_js_filename, 'w', encoding='utf-8') as f:
            f.write(self.DATA_JS_PREFIX)
            f.write(str(content))

    def _copy_overview_img(self, overview_img_path):
        base_name = os.path.basename(overview_img_path)
        shutil.copyfile(
            overview_img_path,
            os.path.join(self.report_dir, base_name)
        )
