# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wraplot']

package_data = \
{'': ['*']}

install_requires = \
['imageio-ffmpeg>=0.3.0,<0.4.0',
 'imageio>=2.6.1,<3.0.0',
 'matplotlib>=3.1.2,<4.0.0',
 'numpy>=1.17.4,<2.0.0']

setup_kwargs = {
    'name': 'wraplot',
    'version': '0.1.1',
    'description': 'A simple python wrapper of matplotlib',
    'long_description': '# wraplot\n\nA simple pythonic matplotlib wrapper: plot, subplot and animate with ease.\n\n## Installation\n\n```bash\ngit clone git@github.com:LucaMoschella/wraplot.git\ncd wraplot\npoetry install \n```\n\n## Sample usage\n\n### Spy\n```python\nspyplot = Spy()\nspyobj = Spy.Object(matrix=dense_matrix > 0.5,\n                    axis_visibility=\'off\',\n                    markersize=4)\no = spyplot(spyobj)\n```\n\n![](sample/spyplot.png)\n\n### Imagesc\n```python\nspyplot = Spy()\nspyobj = Spy.Object(matrix=dense_matrix > 0.5,\n                    axis_visibility=\'off\',\n                    markersize=4)\no = spyplot(spyobj)\n```\n![](sample/imagescplot.png)\n\n### PlotCloud\n```python\ncloudplot = PlotCloud2D()\ncloudobj = PlotCloud2D.Object(points=points,\n                              axis_visibility=\'off\',\n                              xlim=[0, 1],\n                              ylim=[0, 1],\n                              markersize=500)\no = cloudplot(cloudobj, outfile="sample/cloudplot.png")\n```\n![](sample/cloudplot.png)\n\n### Subplotting\n```python\nsubplotter = Subplotter()\no = subplotter(objs=[[spyobj, cloudobj],\n                     [imagescobj, spyobj]],\n               plot_functions=[[spyplot, cloudplot],\n                               [imagescplot, spyplot]],\n               outfile="sample/subplot.png")\n```\n![](sample/subplot.png)\n \n### Animation\n```python\nanimator = Animator()\nfor i in range(50):\n    dense_matrix = dense_matrix @ dense_matrix\n    o = imagescplot(Imagesc.Object(matrix=np.random.rand(100, 100).astype(np.float)))\n    animator.add_figure(o)\nanimator.save("sample/video.mp4", fps=15)\n```\n![](sample/video.gif)\n\n\n# Live sample\n\n```bash\nstreamlit run sample/demo\n```\n\n',
    'author': 'Luca Moschella',
    'author_email': 'luca.moschella94@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/LucaMoschella/wraplot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
