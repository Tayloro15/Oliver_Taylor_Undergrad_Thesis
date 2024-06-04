import subprocess
import xml.etree.ElementTree as ET


def get_image_file_name(xml_file_name):
    """ takes a xml file name and  returns the file names of the all images from xml file as a list"""
    tree = ET.parse(xml_file_name)
    root = tree.getroot()  
    file_name_list = [] 
    for file_name in root.iter('Filename'):
        file_name_list.append(file_name.text)

    return file_name_list

def create_usable_filename(name_string):
    """takes the xml file name and returns the name that the file will be downloaded as"""
    usable_filename = name_string.replace('/','-') + '.jpeg'
    return usable_filename


def run_wget(file_name_list,download_path):
    """takes list of file name from get_image_file_name and the download location of the image and downloads the all of them that were in the xml file"""
    download_count =0
    for file_name in file_name_list:
        usable_filename = create_usable_filename(file_name)
        URL_name = 'http://www.beazley.ox.ac.uk/Vases/SPIFF/'+file_name+'cc001001.jpe'
        full_arg = 'wget '+'-nv --show-progress '+'-O '+download_path+usable_filename+' '+URL_name
        subprocess.run(full_arg, shell=True)
        download_count += 1
        print("downloads:",download_count)
    print("files downloaded:",download_count)


if __name__ == '__main__':
    file_name_list = get_image_file_name('directory path to where the xml files are stored/Oliver_Taylor_Undergrad_Thesis/file_name.xml')
    run_wget(file_name_list,'directory path to where the downloaded images will be stored/Oliver_Taylor_Undergrad_Thesis/Images_downloaded/(Black_Figure/)or(Red_Figure/)')

    
