nano
====

Some tools to compute energy levels for atomic structures drawn with ASCII art

For example, if you run `butterfly.py` it stores a (high resolution version of) this image in `hex.1000.jpg`:

![Output of butterfly.py](https://raw.githubusercontent.com/dpiponi/nano/master/out.jpg)

That was created by drawing this ASCII art

      A-B     C-D     E-B     G-H     I-J     K-L     M-N     O-P     Q-R     S-T     U-V     W-X     Y-Z     a-b    
     /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \    
    o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o
     \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /    
      A B     C D     E B     G H     I J     K L     M N     O P     Q R     S T     U V     W X     Y Z     a b    

That is used to represent an infinite hexagonal lattice. The letters A-Z are used to indicate identified points so the above represents the infinite (in vertical extent) lattice

       \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /  
        o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     a-b  
       /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \  
      o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o
       \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /  
        o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     a-b  
       /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \  
      o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o
       \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /  
        o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     o-o     a-b  
       /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \   /   \ 

See [Hofstadter's butterfly](https://en.wikipedia.org/wiki/Hofstadter%27s_butterfly) for my original motivation for this project.

It's fairly flexible. For example it had no trouble reproducing the energy levels for the graphene spirals in [this paper](https://arxiv.org/abs/1301.2226).
