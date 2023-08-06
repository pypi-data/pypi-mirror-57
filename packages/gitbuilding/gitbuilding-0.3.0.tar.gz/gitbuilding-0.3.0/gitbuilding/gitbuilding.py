 
import codecs
import re
import yaml
import os
import sys
import shutil
from copy import deepcopy
from colorama import Fore,Back, Style


class Config():
    def __init__(self):
        self.categories = {
            'part':{'Reuse':False,'DisplayName':'Parts'},
            'tool':{'Reuse':True,'DisplayName':'Tools'}
            }
        self.fussy=True
        self.defaultCategory = 'part'
        self.debug=False
        self.outDir='Output'
        self.pageBOMTitle = ""
        #TODO make exclude setable
        self.exclude= "README.md"

#global config object- I think I am ok with this!
config = Config()

warninglog = []

#used to trace warnings
activepage = ""

def warn(message,fussy=False):
    #if the waring is tagged fussy and fussy warning are on
    if activepage == "":
        onpage = ""
    else:
        onpage = f"  Warning when scanning page: '{activepage}'"
        
    if fussy and config.fussy:
        print(Fore.YELLOW+"Fussy Warning: "+message+Style.RESET_ALL+onpage)
    else:
        print(Fore.RED+"Warning: "+message+Style.RESET_ALL+onpage)
        
    warninglog.append({'message': message,'onpage': onpage, 'fussy':fussy})

def gberror(message,followup=""):
    #if the waring is tagged fussy and fussy warning are on
    if activepage == "":
        onpage = ""
    else:
        onpage = f"Error when scanning page: '{activepage}'"
    print(Back.RED+"Fatal Error: "+message+Style.RESET_ALL+"\n"+followup+"\n"+onpage)
    sys.exit(1)

def make_dir_if_needed(dir_or_file,isfile=False):
    '''Makes the director if it doesn't exist.
    Handles empty strings for directory'''
    if isfile:
        directory = os.path.dirname(dir_or_file)
    else:
        directory = dir_or_file
    if not directory == '':
        if not os.path.exists(directory):
            os.makedirs(directory)

def parse_inline_yaml(txt):
    """
    This function returns a python dictionary from inline YAML by parsing it
    with YAML flow-style. 

    https://yaml.org/spec/1.2/spec.html#style/flow/

    It also puts in spaces after `:` if forgotten
    
    It also lowers the case of every key
    """
    try:
        in_dict =  yaml.safe_load('{' + txt + '}')
        
        #look for errors where no space is after the key
        key_errors = False
        for key in in_dict.keys():
            #no space after key results in a key with a colon and None for a result
            if ':' in key and in_dict[key] is None:
                key_errors = True
                #add in the space after colon
                txt = txt.replace(key,key.replace(':',': '))
        #if there were key errors then run again
        if key_errors:
            in_dict =  yaml.safe_load('{' + txt + '}')

        out_dict = {}
        for key in in_dict.keys():
            out_dict[key.lower()] = in_dict[key]
        return out_dict
    except:
        return None


def replace_ims(text,replaceall=True,pageDir=None):
    #Page dir sets directory inside the gitbuilding directory to make relative links work
    
    #Find imageas in the text
    #Group 1: all
    #Group 2: alt-text
    #Group 3: image-path
    #group 4: hover text
    ims = re.findall('(!\[([^\]]*)\]\(\s*([^\)\s]+)\s*(?:\"([^\"\n\r]*)\")?\))',text,re.MULTILINE)
    for im in ims:
        imagepath = im[2]
        if os.path.isfile(imagepath):
            if (pageDir is not None) and (not os.path.isabs(imagepath)):
                imagepath=os.path.normpath(os.path.join(pageDir,imagepath))
            #The images path relative to the images directory
            imrelpath = os.path.relpath(imagepath,'images')
            if imrelpath.startswith('..'):
                warn(f"Image: {imagepath} is not in the images directory. Image will be coppied into build but may cause unreliable behaviour")
                imrelpath = os.path.split(imagepath)[1]
            #relative to base folder
            newimrelpath = os.path.join('images',imrelpath)
            newimpath = os.path.join(config.outDir,newimrelpath)
        
            if replaceall or (not os.path.isfile(newimpath)):
                try:
                    make_dir_if_needed(newimpath,isfile=True)
                    shutil.copyfile(imagepath,newimpath)
                except:
                    warn(f"Couldn't copy file '{imagepath}' to output.")
            #now relative to page
            newimrelpath = os.path.relpath(newimrelpath,pageDir)
            text = text.replace(im[0],f'![{im[1]}]({newimrelpath} "{im[3]}")')
        else:
            warn(f"'{imagepath}' is missing.")
        
    return text

def replace_stl_links(text,tofile=True,pageDir=None):
    #Find any link to an STL that starts on its own line. Copy STL to output
    
    #Find stls in the text
    #Group 1: all
    #Group 2: link syntax
    #Group 3: stl file
    stls = re.findall('(^(\[[^\]]*\])\((.+?\.stl)\))',text,re.MULTILINE)
    for stl in stls:
        stlpath = stl[2]
        if (pageDir is not None) and (not os.path.isabs(stlpath)):
            stlpath=os.path.normpath(os.path.join(pageDir,stlpath))
        #The stl path relative to the models directory
        stlrelpath = os.path.relpath(stlpath,'models')
        if stlrelpath.startswith('..'):
            warn(f"STL: {stlpath} is not in the models directory. File will be coppied into build but may cause unreliable behaviour")
            stlrelpath = os.path.split(stlpath)[1]
        #relative to base folder
        newstlrelpath = os.path.join('models',stlrelpath)
        newstlpath = os.path.join(config.outDir,newstlrelpath)
        if tofile:
            try:
                make_dir_if_needed(newstlpath,isfile=True)
                shutil.copyfile(stlpath,newstlpath)
            except:
                warn(f"Couldn't copy file '{stlpath}' to output, does it exist?")
        #now relative to page
        newstlrelpath = os.path.relpath(newstlrelpath,pageDir)
        text = text.replace(stl[0],f'{stl[1]}({newstlrelpath})')
    return text

def find_reference_links(text):
    #Loking for reference style links. These must use "s or 's to define alt-text
    # Note the \\4 rather than \4 when matching the ' or ", not sure why we need this!?
    #Group 1: link text
    #Group 2: link loacation
    #Group 3: either a ' or a ", captured so regex can find the equivalent
    #Group 4: alt text
    ref_link_matches = re.findall('''(^[ \t]*\[(.+)\]:[ \t]*([^\"\' \t]*)(?:[ \t]+(\"|')((?:\\\\4|(?!\\4).)*?)\\4)?[ \t]*$)''',text,re.MULTILINE)
    ref_links =[]
    for ref_link in ref_link_matches:
        alttext = ref_link[4]
        #Search for yaml in alttext
        yaml_match = re.findall("({([^}\n]*)})",alttext)
        if len(yaml_match) == 0:
            yaml=None
        else:
            yaml=yaml_match[-1][1]
            alttext = alttext.replace(yaml_match[-1][0],'')
        if ref_link[2] == '':
            location='missing'
        else:
            location = os.path.normpath(ref_link[2])
        ref_links.append( {'fullmatch':ref_link[0],'linktext':ref_link[1],'linklocation':location,'alttext':alttext,'yaml':yaml} )
    return ref_links

def find_buildup_links(text):
    
    links = []
    link_matches = re.findall('(\[([^]]+?)\](?:\(\s*(\S+)\s*(?:\"([^"]+)\")?\s*\))?{([^:][^}\n]*)})',text,re.MULTILINE)
    for link in link_matches:
        if link[2] == "":
            linklocation = ""
        else:
            linklocation = os.path.normpath(link[2])
        links.append( {'fullmatch':link[0],'linktext':link[1],'linklocation':linklocation,'alttext':link[3],'yaml':link[4]} )
    return links

def create_stl_page(stlfile):
    relpath = os.path.relpath(stlfile)
    lpdir,lpname = os.path.split(relpath)
    if lpdir.startswith('..'):
        warn('Included files should be in the project directory')
    lpoutdir = os.path.join(config.outDir,lpdir)
    make_dir_if_needed(lpoutdir)
    outpath = os.path.join(lpoutdir,lpname)
    if stlfile.endswith('.stl'):
        shutil.copyfile(stlfile,outpath)
        with codecs.open(outpath[:-3]+'md', "w", "utf-8") as outfile:
            output = u''
            output += f'# {lpname[:-4]}\n\n'
            output += f'[Download STL]({lpname})\n\n'
            outfile.write(output)

def buildpart(lib,partname):
    """
    This function makes a markdown page for a part in a yaml file
    """
    try:
        with open(f"{lib}", 'r') as stream:
            partslib = yaml.load(stream, Loader=yaml.SafeLoader)
            
    except:
        warn(f"Cannot make a page for {lib}#{part}. I cannot read {lib}, does it exist?")
        return
    
    
    if partname in partslib:
        try:
            part = partslib[partname]
            if 'Name' in part:
                part_md = f'# {part["Name"]}\n\n'
            else:
                part_md = f'# {partname}\n\n'
            
            if "Description" in part:
                part_md += f'{part["Description"]}\n\n'
            if 'Specs' in part:
                part_md += f'\n\n## Specifications\n\n|Attribute |Value|\n|---|---|\n'
                for skey in part['Specs']:
                    part_md += f'|{skey}|{part["Specs"][skey]:}|\n'
            if 'Suppliers' in part:
                part_md += f'\n\n## Suppliers\n\n|Supplier |Part Number|\n|---|---|\n'
                for skey in part['Suppliers']:
                    if 'Link' in part["Suppliers"][skey]:
                        link = part["Suppliers"][skey]["Link"]
                    else:
                        link = 'missing'
                    if 'PartNo' in part["Suppliers"][skey]:
                        partno = part["Suppliers"][skey]["PartNo"]
                    else:
                        partno = 'Unknown'
                    part_md += f'|{skey}|[{partno}]({link})|\n'
        except:
            warn(f"Unexpected error trying to build page for {lib}#{part}")
                
        libdir = re.match("^(.+)\.ya?ml$",lib).group(1)
        libpath = os.path.join(config.outDir,libdir)
        if not os.path.isdir(libpath):
            os.mkdir(libpath)
        outfilename = os.path.join(libpath,f"{partname}.md")
        if os.path.exists(outfilename):
            outfilename_rel = os.path.join(libdir,f"{partname}.md")
            warn(f"Overwriting {outfilename_rel}, is this part multiply defined?")
        with  codecs.open(outfilename, "w", "utf-8") as outfile:
            outfile.write(part_md)

class Documentation(object):
    
    def __init__(self,conf=None,buildDir=None):
        
        if buildDir is not None:
            assert type(buildDir) is str, 'the build directory must be a string'
            config.outDir = buildDir
            
        confErrMsg = "In buildconf.yaml "
        
        self.project_data = {'Title': None,'Authors': None,'Email': None,'Affiliation': None,'License': None}
        
        if conf is None:
            self.settings = {}
        else:
            #reading config
            with open(conf, 'r') as stream:
                self.settings = yaml.load(stream, Loader=yaml.SafeLoader)
                    
        self.landing = None
        #All the settings stuff could do with tudying up, it is becoming a lot of repeated code
        if 'LandingPage' in self.settings:
            self.landing = self.settings['LandingPage']
        if 'CustomCategories' in self.settings:
            if type(self.settings['CustomCategories']) is dict:
                #TODO: check all categories have correct reuse info.
                for category in self.settings['CustomCategories']:
                    config.categories[category.lower()] = self.settings['CustomCategories'][category]
            else:
                warn(f"{confErrMsg}`CustomCategories` should be entered as a dictionary.")
        if 'DefaultCategory' in self.settings:
            if self.settings['DefaultCategory'].lower() in config.categories:
                config.defaultCategory = self.settings['DefaultCategory'].lower()
            else:
                warn(f"{confErrMsg}The default category should be a defined category.")

        if 'Fussy' in self.settings:
            config.fussy = bool(self.settings['Fussy'])
        if 'PageBOMTitle' in self.settings:
            config.pageBOMTitle = str(self.settings['PageBOMTitle'])
        else:
            config.pageBOMTitle = ""
        
        #Project settings
        self.project_data['Homepage'] = self.landing
        if 'Title' in self.settings:
            if type(self.settings['Title']) is str:
                self.project_data['Title'] = self.settings['Title']
            else:
                warn(f"{confErrMsg}Title should be a string not a {type(self.project_data['Title'])}")
        if 'Authors' in self.settings:

            if type(self.settings['Authors']) is str:
                self.project_data['Authors'] = [self.settings['Authors']]
            elif type(self.settings['Authors']) is list:
                self.project_data['Authors'] = []
                for author in self.settings['Authors']:
                    if type(author) is str:
                        self.project_data['Authors'].append(author)
                    else:
                        warn(f"{confErrMsg}Each author in Authors should be a string")
            else:
                warn(f"{confErrMsg}Authors should be a list or a string not a {type(self.settings['Authors'])}")
        if 'Email' in self.settings:
            if type(self.settings['Email']) is str:
                self.project_data['Email'] = self.settings['Email']
            else:
                warn(f"{confErrMsg}Email must be a string not a {type(self.settings['Email'])}")
        if 'Affiliation' in self.settings:
            if type(self.settings['Affiliation']) is str:
                self.project_data['Affiliation'] = self.settings['Affiliation']
            else:
                warn(f"{confErrMsg}Affiliation must be a string not a {type(self.settings['Affiliation'])}")
        if 'License' in self.settings:
            if type(self.settings['License']) is str:
                self.project_data['License'] = self.settings['License']
            else:
                warn(f"{confErrMsg}License must be a string not a {type(self.settings['License'])}")

    def prepare_directory(self,force=False):
        if os.path.isdir(config.outDir):
            curfiles = os.listdir(config.outDir)
            if curfiles != []:
                
                if not os.path.exists(os.path.join(config.outDir,"_data","project.yaml")):
                    gberror("Output directory is not empty, and doesn't appear to be a valid Git Building output. Empty directory or choose another.",
                            "This a check so we don't delete your files. If you get this error try deleting the output directory.")
                
                with open(os.path.join(config.outDir,"_data","project.yaml"), 'r') as stream:
                    curproject = yaml.load(stream, Loader=yaml.SafeLoader)
                
                if not 'FileList' in curproject:
                    gberror("Output directory doesn't appear to be a valid Git Building output.",
                            "This a check so we don't delete your files. If you get this error try deleting the output directory.")
                
                outfiles = []
                for root, dirs, files in os.walk(config.outDir):
                    for filename in files:
                        if not filename.endswith('project.yaml'):
                            outfiles.append( os.path.relpath(os.path.join(root,filename),start=config.outDir))
                outfiles.sort()
                
                #Unless it is forced the gitbuilding will not delete files in the output directory ready to build, unless they match the files that gitbuilding built last time
                #This way people can't accidentally point gitbuilding at an important directory and delete the contents!
                if not force:
                    if not curproject['FileList'] == outfiles:
                        gberror("Output directory doesn't appear to be a valid Git Building output.",
                            "This a check so we don't delete your files. If you get this error try deleting the output directory.")

                for item in os.listdir(config.outDir):
                    itempath = os.path.join(config.outDir,item)
                    if os.path.isdir(itempath):
                        shutil.rmtree(itempath)
                    else:
                        os.remove(itempath)
                    
        else:
            os.mkdir(config.outDir)
        os.mkdir(os.path.join(config.outDir,"images"))
        os.mkdir(os.path.join(config.outDir,"_data"))
    
    def buildall(self, force=False):
        """
        Builds every page
        `force` overrides checking the files in the output folder
        ONLY USE THIS FOR the server, we don't want people accidentally deleting loads of their files!
        """
        
        global activepage
        self.prepare_directory(force)
        self.pages = []
        
        skipdirs = ['./.git']
        for root, dirs, files in os.walk("."):
            #Check if this directory is in a directory to be skipped
            skip=False
            for skipdir in skipdirs:
                if root.startswith(skipdir):
                    skip=True
                    continue
            if skip:
                continue
            
            #Check if directory containts `_data`
            #If so it is a output directory and should be added to skip list
            if '_data' in dirs:
                skipdirs.append(root)
                continue
            
            for file in files:
                if file.endswith(".md"):
                    if not os.path.basename(file) in config.exclude:
                        self.pages.append( Page(os.path.relpath(os.path.join(root,file), start="."),self))
        
        
        if 'index.md' in self.pages:
            if self.landing is None:
                self.landing = 'index.md'
            elif not self.landing == 'index.md':
                warn(f'Landing page is set to {self.landing} but also `index.md` exists. This may cause unreliable behaviour')
        
        if self.landing in self.pages:
            self.landing_page = self.pages[self.pages.index(self.landing)]
        if self.project_data['Title'] is None:
            if self.landing is None:
                self.project_data['Title'] = "Untitled project"
            else:
                self.project_data['Title'] = self.landing_page.title
        
        # count parts and find steps on all pages
        for p in self.pages:
            activepage = p.filename
            p.count_page()
            
        #build step_tree for all pages
        for p in self.pages:
            activepage = p.filename
            p.get_step_tree()
            
        for p in self.pages:
            activepage = p.filename
            p.count_all()
        
        for p in self.pages:
            activepage = p.filename
            p.finish_build()
        
        activepage = ""
        
        #Create total parts list, the count is meaningless but it is used to know which parts are needed from yaml libraries
        totalpartslist = PartList(AggregateList=True)
        for p in self.pages:
            totalpartslist.merge(p.partlist)
        
        for part in totalpartslist:
            if part.link is not None:
                #match if the part's link is in the format `abc.yaml#abc` or `abc.yml#abc`
                libmatch = re.match("^(.+\.ya?ml)#(.+)$",part.link)
                if libmatch is not None:
                    library = libmatch.group(1)
                    part = libmatch.group(2)
                    buildpart(library,part)
        
        #Add page summary to project data
        self.project_data['PageList'] = []
        for p in self.pages:
            self.project_data['PageList'].append(p.summary())
            
        if self.landing_page is not None and len(self.landing_page.steps)>0:
            self.project_data['NavPages'] = []
            for step in self.landing_page.steps:
                self.project_data['NavPages'].append(self.pages[self.pages.index(step)].summary())
        else:
            self.project_data['NavPages'] = self.project_data['PageList']
        
        outfiles = []
        for root, dirs, files in os.walk(config.outDir):
            for file in files:
                outfiles.append(os.path.relpath(os.path.join(root,file), start=config.outDir))
        outfiles.sort()
        self.project_data['FileList'] = outfiles
        
        with open(os.path.join(config.outDir,"_data","project.yaml"), 'w') as outfile:
            yaml.dump(self.project_data, outfile, default_flow_style=False)

    def get_log_length(self):
        '''returns the length of the warning log'''
        #function part of Documentation so it can be accessed by server
        global warninglog
        return len(warninglog)
    
    def get_log(self,starting=0):
        '''returns the warning log entries from `starting` onwards'''
        #function part of Documentation so it can be accessed by server
        global warninglog
        return warninglog[starting:]
    

class Page(object):
    
    def __init__(self,filepath,doc,empty=False):
        self.filepath = os.path.relpath(filepath)
        self.pagedir,self.filename = os.path.split(filepath)
        self.doc = doc
        
        if empty:
            self.raw_text = ""
        else:
            self.raw_text = self.get_raw()
        self.processed_text = ''
        
        self.partlist = PartList()
        self.all_parts = None
        self.partlinks = []
        self.reflinks=[]
        
        self.steps = []
        self.steplinks = []
        self._step_tree = None
        
        
        self.get_title()
        self.reflinks=[]
        
    def rebuild(self,md):
        """This is to replace the raw text and rebuild. This is used by the live-editor to update a page."""      
        global activepage
        activepage = self.filename
        self.raw_text = md
        self.processed_text = ''
        
        self.partlist = PartList()
        self.all_parts = None
        self.partlinks = []
        self.reflinks=[]
        
        self.steps = []
        self.steplinks = []
        self._step_tree = None
        
        self.get_title()
        self.count_page()
        self.get_step_tree()
        self.count_all()
        result = self.finish_build(tofile=False)
        activepage = ""
        return result
        
    def save(self,md):
        make_dir_if_needed(self.filepath,isfile=True)
        try:
            with codecs.open(self.filepath, "w", "utf-8") as outfile:
                outfile.write(md)
            return True
        except:
            return False
    
    def get_title(self):
        
        headings = re.findall('^#(?!#)[ \t]*(.*)$',self.raw_text,re.MULTILINE)
        
        if len(headings)>0:
            self.title = headings[0]
        else:
            self.title = ''
        
    def __eq__(self,other):
        return self.filepath == other
    
    def get_raw(self):
        try:
            with codecs.open(self.filepath, mode="r", encoding="utf-8") as input_file:
                text = input_file.read()
        except:
            warn(f"Failed to load a page from {filepath}")
            raise
        return text
    
    def summary(self):
        return {'Title': self.title,'Link': self.filepath}
    
        
    def count_page(self):
        
        self.reflinks = find_reference_links(self.raw_text)
        
        for reflink in self.reflinks:
            if not reflink['yaml'] is None:
                rellinklocation= os.path.normpath(os.path.join(self.pagedir,reflink['linklocation']))
                self.partlist.append( Part([reflink['linktext'],rellinklocation,reflink['yaml']]) )
        refnames = [reflink['linktext'] for reflink in self.reflinks]
        
        links = find_buildup_links(self.raw_text)

        # Loop through each part ref
        for link in links:
            if link['linklocation'] == "" and link["linktext"] in refnames:
                link['linklocation'] = self.reflinks[refnames.index(link["linktext"])]['linklocation']
            link_prop =  parse_inline_yaml(link['yaml'])
            if link_prop is None:
                warn(f'Broken part reference: "{link["fullmatch"]}" needs fixing.')
            else:
                if 'step' in link_prop and link_prop['step']:
                    if link['linklocation'] == '':
                        warn(f"The link '{link['fullmatch']}' is a step, but links to nowhere.")
                    else:
                        self.steps.append(link['linklocation'])
                    self.steplinks.append(link)
                else:
                    if link['linklocation'] == "":
                        rellinklocation=""
                    else:
                        rellinklocation= os.path.normpath(os.path.join(self.pagedir,link['linklocation']))
                    self.partlist.countpart([link["linktext"],rellinklocation,link["yaml"]])
                    self.partlinks.append(link)
                
                    
        # Once part refs all scanned, if qty for page was undefined initially set to quantity used.
        self.partlist.finishcounting()
        
        if config.debug:
            print(f"\n\n***** PAGE: {self.title}*****\n")
            for part in self.partlist:
                print(part)
        
    def count_all(self):
        if self.all_parts is None: 
            self.all_parts = PartList(AggregateList=True)
            self.all_parts.merge(self.partlist)
            for step in self.steps:
                if step in self.doc.pages:
                    stepPage = self.doc.pages[self.doc.pages.index(step)]
                    stepPage.count_all()
                    self.all_parts.merge(stepPage.all_parts)
        
    def finish_build(self,tofile=True):
        
        self.processed_text = self.raw_text
        #tofile is set to false if you dont want the builds to be produced (this is used in the live preview)
        self.processed_text = replace_ims(self.processed_text,replaceall=tofile,pageDir=self.pagedir)
        self.processed_text = replace_stl_links(self.processed_text,tofile=tofile,pageDir=self.pagedir)
        
        #Find {{BOM}} syntax to replace with bill of materials text
        BOMs = re.findall('(\{\{[ \t]*BOM[ \t]*\}\})',self.processed_text,re.MULTILINE)
        
        #If bill of material is needed for this page, generate the markdown for it      
        if len(BOMs)>0:
            BOMtext = self.all_parts.BOMmd(config.pageBOMTitle)
        
        #Place bill of materials into page
        for bom in BOMs:
            self.processed_text = self.processed_text.replace(bom,BOMtext)

        #Find {{BOMlink}} syntax to replace with link to Bill of materials page
        BOMlinks = re.findall('(\{\{[ \t]*BOMlink[ \t]*\}\})',self.processed_text,re.MULTILINE)
        
        #If bill of material is needed for this page, generate the markdown for it      
        if len(BOMlinks)>0:
            BOMpagename = self.make_BOM_page()
        
        #Place bill of materials into page
        for bomlink in BOMlinks:
            self.processed_text = self.processed_text.replace(bomlink,BOMpagename)
            
        for link in self.steplinks:
            if link["linktext"] == '.' and link["linklocation"] in self.doc.pages:
                linktext = self.doc.pages[self.doc.pages.index(link["linklocation"])].title
            else:
                linktext = link["linktext"]
            if link["linklocation"] == '':
                self.processed_text = self.processed_text.replace(link['fullmatch'],f'[{linktext}]')
            else:
                self.processed_text = self.processed_text.replace(link['fullmatch'],f'[{linktext}]({link["linklocation"]} "{link["alttext"]}")')
        
        for link in self.partlinks:
            self.processed_text = self.processed_text.replace(link['fullmatch'],f'[{link["linktext"]}]')
        
        #make page for directly linked stls
        for link in self.partlist.links():
            if os.path.exists(link) and link.endswith('.stl'):
                create_stl_page(link)

        #process reflinks
        for reflink in self.reflinks:
            location = reflink["linklocation"]
            if location.endswith('.stl'):
                location = location[:-3]+"md"
            libpartmatch = re.match("^(.+)\.ya?ml#(.+)$",location)
            if libpartmatch is not None:
                location = os.path.join(libpartmatch.group(1),libpartmatch.group(2)+".md")
            clean_reflink = f'[{reflink["linktext"]}]:{location} "{reflink["alttext"]}"'
            self.processed_text = self.processed_text.replace(reflink['fullmatch'],clean_reflink)
                
        #Add reference style link for anything that doesn't have one
        for part in self.partlist:
            refnames = [reflink['linktext'] for reflink in self.reflinks]
            if not part.name in refnames:
                self.processed_text+= "\n"+part.reflinkmd()
        
        if tofile:
            outfilename = os.path.join(config.outDir,self.filepath)
            make_dir_if_needed(outfilename,isfile=True)
            #Write to file in Output folder
            with codecs.open(outfilename, "w", "utf-8") as outfile:
                outfile.write(self.processed_text)
            return None
        else:
            return self.processed_text

    def get_step_tree(self,breadcrumbs=None):
        if self._step_tree is None:
            if breadcrumbs is None:
                breadcrumbs = [self.filepath]
            else:
                if self.filepath in breadcrumbs:
                    gberror(f"The step in this document form a loop!",str(breadcrumbs))
                breadcrumbs.append(self.filepath)
            outlist = []
            if not (self.steps == []):
                for step in self.steps:
                    if step in self.doc.pages:
                        stepPage = self.doc.pages[self.doc.pages.index(step)]
                        outlist.append(stepPage.get_step_tree(breadcrumbs))
                    else:
                        warn(f'Missing instructions {step}')
            self._step_tree = {self.filepath: outlist}
        return self._step_tree
    
    def make_BOM_page(self):
        #Make seperate Bill of materials page
        output=u''
        # Bill of material markdown
        output+= self.all_parts.BOMmd("# Bill of Materials",reflinks=True)
        filename = self.filepath[:-3]+"_BOM.md"
        with codecs.open(os.path.join(config.outDir,self.pagedir,filename), "w", "utf-8") as outfile:
            outfile.write(output)
        return filename


def add_quantities(q1,q2):
    if q1 is None:
        return q2
    if q2 is None:
        return q1
    
    #This is horrible!
    try:
        return q1+q2
    except:
        pass
    try:
        return q2+q1
    except:
        pass
    try:
        return q1+type(q1)(q2)
    except:
        pass
    try:
        return q2+type(q2)(q1)
    except:
        return 'Some'
    
def largest_quantity(q1,q2):
    if q1 is None:
        return q2
    if q2 is None:
        return q1
    
    #This is also horrible!
    try:
        return max(q1,q2)
    except:
        pass
    try:
        return max(q2,q1)
    except:
        pass
    try:
        return max(q1,type(q1)(q2))
    except:
        pass
    try:
        return max(q2,type(q2)(q1))
    except:
        return 'Some'
    

class Part():
    
    def __init__(self,info,indexed=True):
        self.valid=True
        # An indexed part is one that has been added to a partlist
        self.indexed = indexed
        self.name = info[0]
        #set Part defaults
        self.link=None
        self.cat=config.defaultCategory
        self.reuse=False
        #None for total quantity would mean that no total is defined and it is calculated from number used
        self.total_qty=None
        #qty_used is set as None because type has not yet been set
        self.qty_used=None
        self.note = None
        
        self.construct_part(info[1],info[2])
        
    def construct_part(self,partlink,partyaml):
        
        if not partyaml is '':
            part_info = parse_inline_yaml(partyaml)
            if part_info is None:
                warn('Cannot parse {%s}.'%partyaml)
                self.valid=False
                return None
        else:
            part_info = dict()
        
        #Set link
        if not partlink == '':
            partlink = os.path.normpath(partlink)
            if not os.path.isabs(partlink):
                if partlink.startswith('..'):
                    warn(f'Link to "{partlink}" removed as path must be within documentation dir')
                else:
                    self.link = partlink
            else:
                warn(f'Link to "{partlink}" removed as only relative paths are supported')
        
        #interpret YAML differently for reference style links or links in the text
        if self.indexed:
            # if Qty not defined or set as ?, leave qty as None
            if 'totalqty' in part_info:
                self.total_qty = part_info['totalqty']
                del part_info['totalqty']
            if 'cat' in part_info:
                if part_info['cat'].lower() in config.categories:
                    self.cat=part_info['cat'].lower()
                    self.reuse = config.categories[self.cat]['Reuse']
                else:
                    warn(f"No valid category {part_info['cat']}. You can define custom categories in the config file.")
                del part_info['cat']
            if 'note' in part_info:
                if type(part_info['note']) == str:
                    self.note = part_info['note']
                else:
                    warn(f"Ignoring the Note '{part_info['note']}' I expected a string not a {type(part_info['note'])}.")
                del part_info['note']
        else:
            if 'qty' in part_info:
                self.qty_used=part_info['qty']
            else:
                self.valid=False
                warn(f"Part link without quantity [{self.name}]. This will be ignored")
                return None
            del part_info['qty']
        if len(part_info.keys()) >0:
            keynames = ''
            for key in part_info.keys():
                keynames += key+', '
            warn(f"Unused keys '{keynames[:-2]}' in part [{self.name}]",fussy=True)
    
    def __eq__(self,obj):
        assert type(obj) is Part, 'Can only compare a Part to another Part'
        # Check type depends on if an indexed part (one in a PartList) is compared to another indexed part or one not yet indexed (see below)
        checkType = self.indexed+obj.indexed
        assert checkType == 1 or checkType == 2, "Part comparison failed, are you trying to compare two non-indexed Parts?"
        
        
        if checkType == 1:
            #Non indexed part compared to an indexed one.
            #This will be for checking whether to increment the parts used or to index the part as a new part
            #Categories don't need to match here as using "qty" for a part to be counted shouldn't set the category
            
            if self.name != obj.name:
                # names must match
                return False
            
            if self.link == obj.link:
                # categories, names and links match
                return True
            
            if obj.link is None or self.link is None:
                    return True
            
            warn(f"Parts on same page have the same name: '{obj.name}' and different links [{self.link},{obj.link}]. "+
                 f"This may cause weird Bill of Materials issues.")
            return False
        
        else:
            #comparing two parts already in parts lists on different pages.
            
            # categories must match
            if self.cat != obj.cat:
                # names must match
                return False
            
            if (self.link is not None) and (obj.link is not None):
                # If links match then they are reffering to the same part
                if self.link == obj.link:
                    if (self.name != obj.name):
                        if self.link == 'missing':
                            #If two parts don't have links they can be ignored
                            return False
                        warn(f"Two have same link '{obj.link}' and different names "+
                                f"[{self.name},{obj.name}]. One name will be picked for the total Bill of Materials."+
                                f"You can ignore fussy warnings by editing your config",fussy=True)
                    return True
                else:
                    return False
            else:
                #if either link is None check name
                if self.name == obj.name:
                    #items with the same name is a match if at least one link is None
                    return True
                
    def __str__(self):
        return f'''{self.name:}
    link:      {self.link}
    category:  {self.cat}
    reuse:     {self.reuse}
    Total Qty: {self.total_qty}
    Qty Used:  {self.qty_used}
    '''
    
    def combine(self,part):
        #combine is different from counting, combine is the operation when two lists are merged
        # as such all parts should be indexed
        assert type(part) is Part, "Can only add a Part to a Part"
        self.indexed, "Part must be indexed to be added to"
        part.indexed, "Can only add indexed parts"
        assert part==self, "Parts must match to be added"
        
        if self.reuse: 
            self.qty_used = largest_quantity( self.qty_used, part.qty_used)
        else:
            self.qty_used = add_quantities(self.qty_used, part.qty_used)
        
        if self.reuse: 
            self.total_qty = largest_quantity( self.total_qty, part.total_qty)
        else:
            self.total_qty = add_quantities(self.total_qty, part.total_qty)
            
        if self.note is None:
            self.note=part.note
        elif not part.note is None:
            self.note += '  '+part.note
            
        
    def count(self,part):
        #count is only done on a page. For merging two lists see combine
        assert self.indexed, "Only indexed parts can count other parts"
        assert not part.indexed, "Can only count non indexed parts"
        
        if self.qty_used == None:
                self.qty_used = part.qty_used
        else:
            if self.reuse: 
                self.qty_used = largest_quantity( self.qty_used, part.qty_used )
            else:
                self.qty_used = add_quantities(self.qty_used,part.qty_used)
    
    def reflinkmd(self):
        if self.link is None:
            link = 'missing'
        elif self.link.endswith('.stl'):
            link = self.link[:-3]+'md'
        else:
            libpartmatch = re.match("^(.+)\.ya?ml#(.+)$",self.link)
            if libpartmatch is not None:
                link = os.path.join(libpartmatch.group(1),libpartmatch.group(2)+".md")
            else:
                link = self.link
        return f'[{self.name}]:{link}'

                                

class PartList():
    
    def __init__(self,AggregateList=False):
        #aggregate lists are summed lists, a non agregate list cannot become an agregate
        self.aggregate = AggregateList
        #All agregate lists are counted, normal lists should be counted before merging into aggregates or calculating a bill of materials
        self.counted = AggregateList
        self.parts=[]
    
    def __getitem__(self,ind):
        return self.parts[ind]
    
    def __setitem__(self,ind,part):
        assert type(part) is Part, "Can only store Part objects in a PartList"
        self.parts[ind] = part
    
    def __len__(self):
        return len(self.parts)

    def append(self,part):
        assert type(part) is Part, "Can only append Part objects to a PartList"
        #TODO: Check if parts clash
        
        #if there was a yaml error the part is not valid and wont be appended
        if part.valid:
            self.parts.append(deepcopy(part))
        
    def merge(self,inputlist):
        assert type(inputlist) is PartList, "Can only merge a PartList to another PartList"
        assert self.aggregate, "Only aggregate lists can merge other lists into them"
        assert inputlist.counted, "List must be counted before being merged into an aggregate"
        for part in inputlist:
            if part in self:
                ind = self.parts.index(part)
                self[ind].combine(part)
            else:
                self.append(part)
        
    def countpart(self,info):
        assert not self.counted, "Cannot count part, counting has finished"
        part = Part(info,indexed=False)
        if part.valid:
            # if the part is already listed, update quantites
            if part in self.parts:
                ind = self.parts.index(part)
                self[ind].count(part)
            else:
                part.indexed=True
                self.append(part)
    
    def finishcounting(self):
        if self.counted:
            return None
        #once counting is finished, if the total quantity was undefined set it to the quantity used
        for part in self.parts:
            if part.total_qty is None:
                part.total_qty = part.qty_used
            if not part.total_qty == part.qty_used:
                warn(f"{part.name} has a total quantity of {part.total_qty} specified but only {part.qty_used} are used.",fussy=True)
        self.counted=True
    
    def partlinkmd(self):
        linktext = u''
        for part in self.parts:
            linktext+=f'{part.reflinkmd()}\n'
        return linktext

    
    def links(self):
        links = []
        for part in self.parts:
            if part.link is not None:
                links.append(part.link)
        return links
        
    def BOMmd(self,title,divide=True,reflinks=False):
        assert self.counted, "Cannot calculate bill of materials for uncounted partlist."
        BOMtext = ''
        if title is not "":
            BOMtext+=f'{title}\n\n'
        # Loop through parts and put quantities and names in/
        for cat in config.categories:
            if "DisplayName" in config.categories[cat]:
                catname = config.categories[cat]["DisplayName"]
            else:
                catname = cat
            first = True
            for part in self.parts:
                if part.cat == cat:
                    if first:
                        first=False
                        BOMtext+=f'\n\n### {catname}\n\n'
                    if part.total_qty is None:
                        continue
                    elif type(part.total_qty) is int:
                        qty_str = str(part.total_qty)+' x '
                    elif type(part.total_qty) is float:
                        qty_str = str(part.total_qty)+' of '
                    else:
                        qty_str = str(part.total_qty)
                        
                    if part.note is None:
                        note_txt = ''
                    else:
                        note_txt = '  '+part.note
                    BOMtext+=f'* {qty_str} [{part.name}]{note_txt}\n'
        if reflinks:
            for part in self.parts:
                BOMtext+=self.partlinkmd()
        return BOMtext


