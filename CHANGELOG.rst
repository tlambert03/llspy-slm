LLSpy Release History
#####################

`0.1.0`_
========

First release as independent package (independent from main LLSpy package)

**Added:**

* Hex pattern generator added to SLM Pattern Generator
* Ronchi-ruling pattern generator added to SLMgen
* Batch SLM pattern generation
* Docs for SLM generator GUI
* Docs for Registration
* Option to dither SLM preview in SLM Pattern Generator
* User-adjustable LUTs for SLM pattern previews

**Changed:**

* SLM pattern generator moved into seperate package: *slmgen*
* Better multi-threading when batch-writing SLM patterns

**Fixed:**

* SLM pattern generator now writes 1-bit file usable on SLM, instead of 8-bit png (thank you for reporting Felix!)


.. _0.1.0: https://github.com/tlambert03/llspy-slm/releases/0.1.0
