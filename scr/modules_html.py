#!/usr/bin/env python3
#import os
#os.environ['OPENBLAS_NUM_THREADS'] = '1'


def html_css ():
    html = '''
<html>
    <head>
        <style>
            body{ margin:0; background:white; color:black; font-family: Arial;}
            .active {
                background-color: #04AA6D;
                color: white;
                }

            /* Vertical bar */
            ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                width: 13%;
                background-color: #1c1f27;
                height: 100%; /* Full height */
                position: fixed; /* Make it stick, even on scroll */
                overflow: auto; /* Enable scrolling if the sidenav has too much content */
                }
            li a {
                display: block;
                color: #ffffff;
                padding: 8px 16px;
                text-decoration: none;
                }

            /* Change the link color on hover */
            li a:hover {
            background-color: #04aa6d;
            color: white;
            }

            .main{
            margin-left: 15%;
            padding: 1px 16px;
            height 500px;
            }

            .fraction {
                display: inline-block;
                vertical-align: middle;
                margin: 0 0.2em 0.4ex;
                text-align: center;
                }

            .fraction > span {
            display: block;
            padding-top: 0.15em;
            }

            .fraction span.fdn {border-top: thin solid white;}
            .fraction span.bar {display: none;}

            .column {
                float: left;
                }
            .center {
                margin: auto;
                width: 15%;
                }
            .c{
              width: 50%;
              display: block;
              margin: auto;
            }
        </style>
        <link rel="icon" href="https://github.com/FerAmbriz/AutoMethyc/blob/master/img/AutoMethyc.png?raw=true">
    </head>
    '''
    return html

def html_navbar_complete ():
    html = '''
    <body>
        <ul class="vertical">
            <li><a href="#Home" style="background-color:#009DCF; color:white"> AutoMethyc </a></li>
            <li><a href="#Base"> Base quality </a></li>
            <li><a href="#Depth"> Depth </a></li>
            <li><a href="#Samples" > Coverage </a></li>
            <li><a href="#cgi" > CGI mapping </a></li>
            <li><a href="#All"> Methylation percentage </a></li>
            <li><a href="#Mean"> Mean methylation </a></li>
            <li><a href="#all_norm"> Normalized methylation </a></li>
            <li><a href="#Mean_norm"> Mean normalized </a></li>
            <li><a href="#pca"> PCA </a></li>
            <li><a href="#about"> About </a></li>
        </ul>
    </body>
    '''
    return html


def html_navbar_sNorm ():
    html = '''
    <body>
        <ul class="vertical">
            <li><a href="#Home" style="background-color:#009DCF; color:white"> AutoMethyc </a></li>
            <li><a href="#Base"> Base quality </a></li>
            <li><a href="#Depth"> Depth </a></li>
            <li><a href="#Samples" > Coverage </a></li>
            <li><a href="#cgi" > CGI mapping </a></li>
            <li><a href="#All"> Methylation percentage </a></li>
            <li><a href="#Mean"> Mean methylation </a></li>
            <li><a href="#about"> About </a></li>
        </ul>
    </body>
    '''
    return html

def html_AutoMethyc (command):
    html = f'''
    <div class="main">
        <h1 id="Home"; style="margin-bottom: 5px;"> AutoMethyc </h1>
        <hr style="margin-top: 0;">
        <div class="center">
            <img src="https://github.com/FerAmbriz/AutoMethyc/blob/master/img/AutoMethyc.png?raw=true" width="110" height="100">
        </div>
        AutoMethyc is an integrative pipeline to methylation analysis from raw paired-end sequences obtained from massive parallel bisulfite sequencing.
    </div">
    <h2 style="margin-bottom: 5px;"> Parameters </h2>
    <hr>
        Command used and global parameters:
    <p style="color:white; background:#2E3440; padding: 15px; border-radius: 15px;"><code>{command}</code></p>
    '''
    return html

def html_base ():
    html = '''
    <body>
        <h2 id="Base"; style="margin-bottom: 5px;"> Base quality </h2>
        <hr style="margin-top: 0;">
        Logarithmic ratio of Phred Q quality scores to base call error probabilities.
    </body>
    '''
    return html

def html_depth ():
    html = '''
    <body>
        <h2 id="Depth"; style="margin-bottom: 5px;"> Depth </h2>
        <hr>
        Count of filtered (off-targets) and unfiltered (on-targets) sites according to the depth threshold established for greater certainty in the analysis.
    </body>
    '''
    return html

def html_coverage ():
    html = '''
    <body>
        <h2 id="Samples" ; style="margin-bottom: 5px;"> Coverage </h2>
        <hr>
        Count of sites present in the regions of interest provided by BED file
    </body>
    '''
    return html

def html_cgi():
    html = '''
    <body>
        <h2 id="cgi"; style="margin-bottom: 5px;"> CGI mapping </h2>
        <hr>
        Mapped regions and their classification considering the nearest CpG island
         <div class="row">
            <div class="c">
                <img src="https://github.com/FerAmbriz/AutoMethyc/blob/master/img/IslaCpG.jpeg?raw=true" width="650" height="150">
            </div>
            </ol>
        </div>
    </body>
    '''
    return html
def html_all():
    html = '''
    <body>
        <h2 id="All"; style="margin-bottom: 5px;"> Methylation percentage </h2>
        <hr>
        Methylation percentage considering the cytosines methylated and unmethylated for each site
    </body>
    '''
    return html

def html_mean_gene():
    html = '''
    <body>
        <h2 id="Mean"; style="margin-bottom: 5px;"> Mean methylation </h2>
        <hr>
           Average percentage of methylation present in each gene of the sequenced region.
    </body>
    '''
    return html

def html_norm():
    html = '''
    <body>
        <h1 style="margin-bottom: 5px;"> Normalization </h1>
        <hr>
            Normalization was performed considering the mean and standard deviation of the controls
    </body>
    '''
    return html

def html_mean_norm():
    html = '''
    <body>
        <h2 id="Mean_norm", style="margin-bottom: 5px;"> Mean normalized </h2>
        <hr>
            Mean normalization of each normalized site belonging to each gene
    </body>
    '''
    return html

def html_pca():
    html = '''
    <body>
        <h2 id="pca"; style="margin-bottom: 5px;"> PCA </h2>
        <hr>
            Principal component analysis (PCA) applied to each site of the normals and samples. Each point represents a normalized site according to the corresponding group (normal or sample).
    </body>
    '''
    return html

def html_fooder():
    html= '''
    <body>
        <h3 id="about"; style="margin-bottom: 5px;"> Repository  </h4>
        <hr>
            This program is avalible in <td><a href="https://github.com/FerAmbriz/AutoMethyc"> AutoMethyc </a></td>
         <div class="row">
            <div class="center">
                <img src="https://github.com/FerAmbriz/AutoMethyc/blob/master/img/Escudo-UNAM.png?raw=true" width="65" height="75">
                <img src="https://github.com/FerAmbriz/AutoMethyc/blob/master/img/LN_FESI.jpg?raw=true" width="75" height="80">
            </div>
        </div>
    </body>
</html>
    '''
    return html
