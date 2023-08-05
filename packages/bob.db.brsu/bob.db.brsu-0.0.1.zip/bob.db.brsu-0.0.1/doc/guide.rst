.. vim: set fileencoding=utf-8 :
.. Tue 03 Jan 2017 16:36:40 CEST

==============
 User's Guide
==============

This package contains the access API and descriptions for the 
`BRSU Skin/Face/Spoof database <https://www.h-brs.de/en/isf/h-brs-haut-gesichts-und-faelschungs-datenbank>`_. 

It only contains the Bob_ accessor methods to use the DB directly
from python. The actual raw data for the dataset
should be downloaded from the original URL.

Note that, at the moment, there are only two "protocols":

- 'train': loads all the data for training purposes
- 'test': loads all the data for testing purposes

.. Place your references here
.. _bob: http://www.idiap.ch/software/bob
