![BLADE](https://raw.githubusercontent.com/bluwireless/blade/master/documentation/source/_static/images/BLADE.png)

---

# BLADE Templating
One of the many possible benefits to using BLADE is the ability to automatically generate RTL (Register Transfer Language), documentation, SDK support, and more for your design. Generated files can take advantage of the hierarchical description of the design, connectivity information, address maps and much more.

The example designs provided with BLADE provide an example of how this templating engine can be integrated with a hardware design flow.

BLADE Templating is built on top of Mako - a flexible and powerful Python templating engine. Traditionally it has been used for generating web pages, but it is more than flexible enough to cope with generating Verilog, VHDL, SystemC, and more. Further details can be found [here](https://www.makotemplates.org).

## System Requirements
Like BLADE, the templator is a Python based tool and has a few dependencies:
 * Python 3.6 or greater
 * [Mako](https://pypi.org/project/Mako/) - The underlying templating engine
 * [DesignFormat](https://github.com/bluwireless/designformat) - The interchange format used by BLADE

