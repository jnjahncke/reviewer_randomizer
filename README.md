# reviewer_randomizer

This script takes in a list of applicants, a list of reviewers, and the number of people to be assigned to each applicant. Reviewers are then randomly assigned to the applicants. Reviewers can be either faculty or non-faculty ("trainees"). Only one non-faculty reviewer can be assigned to each applicant at maximum. 

There are multiple ways to run this code. Fair warning that for longer lists of applicants it can take a *while* to run.

## Running on Shinylive

Definitely the most user friendly method of running the code. Follow [this link](https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMAYgEIB6AVwGcAnBgIwEsIHKAbgAIcZABakAOhGnSaNIQFplK1WvUah8uQoAyxKABMRUQgGsoAczgshd+w8daaOpRvceVz6QDM2xGCEWMV5sIW4YVGI2MiEAQXQ8IQBJCFQmMhYkgHkM9MykgGUbFm5SJLY4UzJuATgKykM4NgaARySmbl9-QLYoCEMA8Mjo2L6B8etuoZgocWGomKEfABtiaOkIxdjUfsMoWwORQ02Rpcrp3rgBbjgAd2aAfXHBmG4AL2aF0aEAKlkIPI3J4QWpvICFABxOCxXj5WxORGObQQ4Gg9HgtCoR6dIQAXiEnSwVjgjx83AAHnBDAAKaQOIliABMdLAACVrrcHmwhGy9gEPs1JGAAJR4en2ImoVkAUXIXygQhW3BYsWIPiElRu92athpeyE4jg3B5-hWcDFQkVytVQnVVvQysI-QKVoGhrEcCEECYME4X3tWq5usNxCE-qtLFKlgg1NDQiqhDEDtQTpdGHiju4zvItju3BWK3DXpeARWYQO0djxhYTCTHrmHrgYVI5aEYigdStsVmFIivrtse9pEUPlMTBWZDCQZ1bAwwrFErsRP8dzpECRRJIK19EBpAFY8ES4RlHhQKWRHlBKlBWTPuSxheL2ZzZyxEE-hV+wABpTkbgB1NhuEsMQyEkSQyAAMXHSdsGkP9CzCABZUgzAg6DYKnaQAClKAgbgfC+HCoDECBzDgDDCjIJgmnIb8n1XFg8SZAAGEVFw3REt2IHcYD3Q9CW4DAT0vc9L2vKpWSxNNc0-MAElTbMXXfeTvwAIWbUhCC9H8IGIO5zUfCAABUoGwNYeUKfMfHAiA2WwfpeWbfSVkMR8wG-PAmJY9jOM3YTt13GkmSPYTRLPOALyvG9WWbGx5IAOV9f0eXtDltQfEQvkU2SyA-fAAGZvIM5iAEYOP8yVhOlYUoIATWSRAhBMkJbBzQ0oDML1FSIu4hDeH0KBYedRXFLjl3CtJT2qMoIEeTgMjIUhWUsYgnyEYVIWIOgNsIFZK0ePFhU4MgIEUWtCB0qMF3GhlhOIPJTzIKBOHNaT0Gea5bqXISMEesh8ki6K6jYTg5giO9rivdAF2kEUASBdFka8FEgQABWA8gGBYTsSxsCdMiRZEXFRFGUfBJoNRYZpQZpUSkgB-IkhpqM5pFD8Js2rmAAEb0IGo6gwABhKAVkIX6+cTQW4Awa5KDIGkDr9fZmtEjA1ppS0QP0ypHn02M8RglYaYRrmqcjKt4HILXOaRe8QwJdWHbYFgtd+hwZOU3N8XCaayAwL2c0yd2uYceLbCdm31YjrWzY9+w5goSJYgJY2aYTuw7hCc1u2T1BU7TsWabt4m7CTuAU99ysda+zLmhpF2shTPLm4js2kSDl1HkMbMyAaeu2B7vvq7IfO7PtmEmDYPcu-IYeBYH4Mh97gX495pmMklyoBmaDAXreyjzbgDUsTr23M+5zus2DhfU8tnXrcVkVgFYgBdS+I993hFZj7AbDjgCJEqpaIK0jkqFUis56XlXgHbq2A3YcSAYiLU4DgDCgysvTaYA35-ATP-YySIfQwDQaqNgNIKQimWNEIQFI-aan6NYGkZU8ARwANQVQ-mHewWp9awBsL7YAFI2FhB8DQikeAwi8CEO8bg0pUF4GISwEUXDL7bj4fAO+vsQAAF9L5iJ5HQ6Rkw4A0nbqXMu6joCaNgUI3BBJeHWJsHY5BThKi1knL7VAhgMAABE5hQCgn0eA+ob7d1gSJZOiC7pl0cEFfiaDhS5W9uBfA2DMFvmFG-DuKCCaeIJN4jAJByJzBpMAdxhMkiFP8S9IJ-DG55IDhkh8+9eKQLjm-GJsTE59nARVS+FT8makaRgHe9SrH8LvkkKAvS8T9O4XYQZ98lkYEMP4aUB1-Qm2Oi+QeHlpmzPmQMqeM8GkeLIDkuwktN4T3sFLXec5xK-QtrwrEF8ZALOGYPLRBIa4xiflrYAZVVGfKWb7BinyDFfKwcY183I74WOJmCthDi4VfDYdgiCMhPKfIcFC6B9CXZ33KWitgb9EXdORQSL8kFhRCAxQSjFNLsWuMcJUGipylnryxL7RSoTsSdBZrTZoZswA6LwOAJx1BKitE6JUJ+I0yAXnwEQUgFAqDIAAFa8E1VAJk0gxUSsgPw6VpLnj8jeJ8OcOAVXFPVWQag9BmDsC4LwfgEBhCiAkB81w5NQTgiBPoIwJhzAkgRN0uwaMFB+pBOCPwQxSyBC2D8F4JjLgDTmMmZNSxVjrDYKcbYwyAS+pjR4ANChfEn14F6HwTByI1FIBG8taJS1ghRNIC2fz5ouwaXs6ZYTcxJHMaypuvsm6jLgKmUwpiaWpKSHShcGAWBKUVsyuGXNoHgM3ROqdOlWQYXktgkUS6V37tkKKEdpK0EUlGWQuRWsMAmzIMBaUVCoVGI3E3LhnsB1EwJEI29z773HqfS+rW1DDH0M3SChwSNW2aBRLBhQotxYTjmD1Nm-yFZKkoJYcQthEP2Dg-BttpMHBEuIb7c0e4m6XJbik-WA4CTUf5a3Ojg1GOBAJLm6IrGGOUd+PggRDBoWzk43R+VUBeBNB5ASPjt8BNCeUUIAApKJ+FxDfoKAkP1WYEBpxXqEPmQsxYH4xjjEaDNFJONJB0xm-TA1eCcYAPy-S7Y8XsY7K5SYeW5zD81Bpee+ZRxQwzZjSaFB8pDLaSOhcI5GhQ6lOhuUJKgBMKcwg2kyAwWB4b4vOBiyR8E5GzUkDrX+oQuitBCG6pOw0fRzB2g1HZvTYQQF0SJomZMLtwiHH89SX6RLYHaJ0dV2raXrSQKawmUwyYCVdos2GLr6nIsle+VlwRuCFAbftGLIsTdfpjkIITbAjwNv-q20EJgnAaaxB2xqI7J2Vuu1+s+nzcBSTnaEMAS7tYbswggbae0b3q1ehpAbUcWFsBUIO1zLTJhXb40Ht6fhzczQ2AANzhmS8YJgaWetZZYDlvuc1ry3EIfYKFPXYV7IpURhHNMUfwAqLxI+SIoViLrcYWFGByQDG4BQch+awAAD0ykQUKBBFgb82EI0kG7CXsuAAkjFSUc0vmt5ejwyu5mAJzgYGt-B4+Yce12QHX32KEKxDXPCzW2P1z4ywRvpQVUA2BlRm2beLLNVlwO6BGg0gd4bx6LvTd3tfXRpECgu3xke3BM7U2aEg9jJ9yBXvwgPcegbp3IeQogYMg3ED4eH1m-d-ialYA4-YSQOnvFUOE+qj96gAPQec-G9d6X4DkfERwBNnAOnZdk8fYbwHLELes+O+dybt3XfWXR-889+MxojQ8gjAt4wlnPM0MC8Q1K03N3w-BjTYwjbnSoYOg2iAhxODEDqL9XsI+gta6y8ARA7nezfvsBxr7RKX-v5mYgJ-lchur+j8pVqNgoONlaIDmqBqMtj1uvkvrNvRsHG5qATrhVlVpAR9mlm9o1vaC1v0AZnsu2HjMWJQGZtWIdjQgStIpugPigd3BgSwMANApbtbp8tAsSmwZ7lFkRtGrFuoMVvwfEAvpuvGKOvlsRoIajGRvYPDkPgIuSGbr9NwL7BwXiknn0KDvQooSPgwbwl9j9pfIRPVu9l6NIt-pAgwZ7P5pxr7Bxppp8r3qYYofQg-lljYYnHYZRgSI4QOBimVJfNnAWF6CxkNn3MAIodkkIAADyUGcbNTp5qEopCBBG4r2D5zVy-osGpqMKmJcHEIqLp4hG5xZE06P40HoFZ6ZBRGVyoC4J0AEisReFOApEEjpFNp2BZG-I5HlJ7AmLybdxFFAERqmFqEAB8jB88imLGehWWVCgmX8gmZUrEaxrRk8HKe46cFoV8sSphXBzBdRkQ9iBIEcGxP6SkwcI08qt+pi+c3eZchRTGOGs8ORjxbK0MvuY+AwNIDx6ehxNRLB+cuCqRnRsSRKRx0R9KHRAJoBtiIJTeAeihHxmuYmCJ2hKeb8SJvx-xfBkaywUOqh6h1BPIVeUiG45J+hxyAgj+F2JhD2UO7hTmnhAJPhLx-hMAn8yojJx2cE7hMy1JGR5c7JXGjm80lGgRwROcYRlAvaWu9uUOMR8R7mxCSRwp4QMJaR6ePR0xtReREATCzxMAxRGppRXo5Rn6XxiePIgJ5WwJ9RpxSmFx9g7R2pGpDgupm6-REw+RQxMxvoppXRGempUxxpeC4RPukCixSmeCqx6xtebiJy2xxcFoyRp81R9pxxDR5ezpiZ5cORE6MAdxfx9RqJiI4ZzGcpm65Z3utJ3x-uuJZZcJVxTBQJ2ZoJsJGpkJ7Z5JnZ7p3SXBCJjpOJtI5JtZz2xKfZo5pZkQEmyZ-pMCfcS86Jfc68HaJ8GavA7ybmY89R98Oxv05pec+5uZOxDBFcVcvydhPaTc-arZg6SmdGQ5y5k5w2vye5KcAIphjwGipIjwuZAA5L+eFvNI8IBYiqBaHGKm-EAA) to run the code on shinylive.

## Running in a Google Colab Jupyter Notebook

To run the script from an editable jupyter notebook in your web browser use [this google colab link](https://colab.research.google.com/drive/1BwNiAB5Pw-tr2n84-bI_EGcn1M7KSTvN). Note that this is EDITABLE. If you break it, it's up to you to fix it. The original version is [saved in this github](https://github.com/jnjahncke/reviewer_randomizer/blob/main/reviewer_randomizer_GoogleColab.ipynb) - use that to fix the shared notebook.

Two output tables and one text file are saved: (1) a table of applicants followed by assigned reviewers and (2) a table of reviewers followed by assigned applicants and (3) text file of reviewers and their assigned applicants. *Output files all contain the same information in different formats.* 

Example output files: [applicants_reviewers.csv](https://github.com/jnjahncke/reviewer_randomizer/blob/main/applicants_reviewers.csv), [reviewer_applicants.csv](https://github.com/jnjahncke/reviewer_randomizer/blob/main/reviewer_applicants.csv), [reviewer_applicants.txt](https://github.com/jnjahncke/reviewer_randomizer/blob/main/reviewer_applicants.txt)

The `reviewer_randomizer.py` script can be run from the command line but the script needs to be edited first to change the inputs since they are hard coded.

#### *Old version(s): did not incorporate trainee reviewers; division of labor not optimized*

*To run the old script from an editable jupyter notebook in your web browser use [this google colab link](https://colab.research.google.com/drive/17uKKnFAhS8MqKoNv1NC1AT_mjG3Ue4nh). Note that this is EDITABLE. If you break it, it's up to you to fix it. The original version is [saved in this github](https://github.com/jnjahncke/reviewer_randomizer/blob/main/reviewer_randomizer_GoogleColab_old.ipynb) - use that to fix the shared notebook.*

*The `reviewer_randomizer_old.py` script can be run from the command line but the script needs to be edited first to change the inputs since they are hard coded.*
