LLSpy Release History
#####################

`0.1.1`_
========

**Changed:**

* renamed main funcs in slm.py
* increased crop precision in gui to 0.001

**Fixed:**

* on windows, the batch write function creates unpredictable output files due to weird windows multi-threading.  For now, restricting batch write to a single thread on windows... will make things slower than Mac or Linux.
* Fix bug that that prevented writing Hex patterns to file
* Fix bug when batch shift/tilt ranges have a single number <= 0

`0.1.0`_
========

First release as independent package (independent from main LLSpy package)

**Added:**

* Hex pattern generator added to SLM Pattern Generator
* Ronchi-ruling pattern generator added to SLMgen
* Batch SLM pattern generation
* Docs for SLM generator GUI
* Option to dither SLM preview in SLM Pattern Generator
* User-adjustable LUTs for SLM pattern previews

**Changed:**

* SLM pattern generator moved into seperate package: *slmgen*
* Better multi-threading when batch-writing SLM patterns

**Fixed:**

* SLM pattern generator now writes 1-bit file usable on SLM, instead of 8-bit png (thank you for reporting Felix!)


.. _0.1.0: https://github.com/tlambert03/llspy-slm/releases/0.1.0
