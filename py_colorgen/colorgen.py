import argparse
import random


parser = argparse.ArgumentParser(description="Random color combination generator")
parser.add_argument("-r",
                    "--rgb",
                    default=False,
                    action="count",
                    help="-r or --rgb to generate rgb color")
parser.add_argument("-s",
                    "--hsl",
                    default=False,
                    action="count",
                    help="-s or --hsl to generate hsl color")

args=parser.parse_args()


def contact_book(rgb,hsl):
    """
    Generate a color combination
    """
    
    def rgb_colour():
        r=random.randint(0, 255)
        g=random.randint(0, 255)
        b=random.randint(0, 255)
        return f"rgb{(r, g, b)}"
    def hsl_colour() :
        h = random.randint(0,360)
        s = "%s%%"%random.randint(0,100)
        l = "%s%%"%random.randint(0,100)
        z=f"\N{DEGREE SIGN}"
        hsl =f"({h}{z},{s},{l})"
        return f"hsl{hsl}"
    
    
    if rgb:
        return rgb_colour()
    if hsl:
        return hsl_colour()
    else:
        hex = ''.join("#"+(format(random.randint(0, 16777215), "x")))
    return hex

    
        





if __name__ == '__main__':

    print(contact_book(args.rgb,args.hsl))
    exit(0)
