# Contributing to The Responding Dark Laughter <!-- omit in toc -->

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents)
for different ways to help and details about how this project handles them. Please
make sure to read the relevant section before making your contribution. It will
make it a lot easier for us maintainers and smooth out the experience for all involved.
The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine.
> There are other easy ways to support the project and show your appreciation, which
> we would also be very happy about:
>
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
    - [Prerequisites](#prerequisites)
    - [Getting Started](#getting-started)
  - [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
  - [Commit Messages](#commit-messages)
  - [Python](#python)
  - [Shell](#shell)
  - [Markdown](#markdown)
  - [Docker](#docker)
  - [Makefile](#makefile)
- [Join The Project Team](#join-the-project-team)

## Code of Conduct

This project and everyone participating in it is governed by the
[The Responding Dark Laughter Code of Conduct](https://github.com/mstrzele/TRDL/blob/master/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable
behavior to [Maciej Strzelecki].

## I Have a Question

> If you want to ask a question, we assume that you have read the available [documentation](https://mstrzele.github.io/TRDL).

Before you ask a question, it is best to search for existing [issues](https://github.com/mstrzele/TRDL/issues)
that might help you. In case you have found a suitable issue and still need clarification,
you can write your question in this issue. It is also advisable to search the internet
for answers first.

If you then still feel the need to ask a question and need clarification, we recommend
the following:

- Open an [issue](https://github.com/mstrzele/TRDL/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (nodejs, npm, etc), depending on what seems
  relevant.

We will then take care of the issue as soon as possible.

## I Want To Contribute

### Legal Notice <!-- omit in toc -->

When contributing to this project, you must agree that you have authored 100%
of the content, that you have the necessary rights to the content and that the
content you contribute may be provided under the project license.

### Reporting Bugs

#### Before Submitting a Bug Report <!-- omit in toc -->

A good bug report shouldn't leave others needing to chase you up for more information.
Therefore, we ask you to investigate carefully, collect information and describe
the issue in detail in your report. Please complete the following steps in advance
to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using
  incompatible environment components/versions (Make sure that you have read the
  [documentation](https://mstrzele.github.io/TRDL). If you are looking for support,
  you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same
  issue you are having, check if there is not already a bug report existing for
  your bug or error in the [bug tracker](https://github.com/mstrzele/TRDL/issues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users
  outside of the GitHub community have discussed the issue.
- Collect information about the bug:
- Stack trace (Traceback)
- OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
- Version of the interpreter, compiler, SDK, runtime environment, package manager,
  depending on what seems relevant.
- Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with older
  versions?

#### How Do I Submit a Good Bug Report? <!-- omit in toc -->

> You must never report security related issues, vulnerabilities or bugs including
> sensitive information to the issue tracker, or elsewhere in public. Instead sensitive
> bugs must be sent by email to [Maciej Strzelecki].

We use GitHub issues to track bugs and errors. If you run into an issue with the
project:

- Open an [issue](https://github.com/mstrzele/TRDL/issues/new). (Since we can't
  be sure at this point whether it is a bug or not, we ask you not to talk about
  a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the _reproduction steps_
  that someone else can follow to recreate the issue on their own. This usually
  includes your code. For good bug reports you should isolate the problem and create
  a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there
  are no reproduction steps or no obvious way to reproduce the issue, the team will
  ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro`
  tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as
  well as possibly other tags (such as `critical`), and the issue will be left to
  be [implemented by someone](#your-first-code-contribution).

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for The
Responding Dark Laughter, **including completely new features and minor improvements
to existing functionality**. Following these guidelines will help maintainers and
the community to understand your suggestion and find related suggestions.

#### Before Submitting an Enhancement <!-- omit in toc -->

- Make sure that you are using the latest version.
- Read the [documentation](https://mstrzele.github.io/TRDL) carefully and find
  out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/mstrzele/TRDL//issues) to see if the
  enhancement has already been suggested. If it has, add a comment to the existing
  issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up
  to you to make a strong case to convince the project's developers of the merits
  of this feature. Keep in mind that we want features that will be useful to the
  majority of our users and not just a small subset. If you're just targeting a
  minority of users, consider writing an add-on/plugin library.

#### How Do I Submit a Good Enhancement Suggestion? <!-- omit in toc -->

Enhancement suggestions are tracked as [GitHub issues](https://github.com/mstrzele/TRDL/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many
  details as possible.
- **Describe the current behavior** and **explain which behavior you expected to
  see instead** and why. At this point you can also tell which alternatives do not
  work for you.
- **Explain why this enhancement would be useful** to most The Responding Dark Laughter
  users. You may also want to point out the other projects that solved it better
  and which could serve as inspiration.

### Your First Code Contribution

1. Install [prerequisites](#prerequisites).
2. [Get started](#getting-started)!

#### Prerequisites

- Linux (e.g. [Ubuntu](https://ubuntu.com) on [Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install))
  or macOS
- Shell (e.g. [GNU Bash](https://www.gnu.org/software/bash/) or [Zsh](https://www.zsh.org))
- [Git](https://git-scm.com)
- [Commitizen](http://commitizen.github.io/cz-cli/)
- [pre-commit](https://pre-commit.com)
- [direnv](https://direnv.net)
- [Python](https://www.python.org)
- [ApacheBench](https://httpd.apache.org/docs/2.4/programs/ab.html)
- Text editor (e.g. [Vim](https://www.vim.org) or [Visual Studio Code](https://code.visualstudio.com))

#### Getting Started

1. [Clone the repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#_git_cloning),
   go to the directory and install Git hooks:

   ```shell
   $ git clone https://github.com/mstrzele/TRDL.git
   Cloning into 'TRDL'...
   # ...
   $ cd TRDL/
   $ pre-commit install
   pre-commit installed at .git/hooks/pre-commit
   ```

2. [Create and activate a Python virtual environment](https://flask.palletsprojects.com/en/2.3.x/installation/#create-an-environment):

   <!-- markdownlint-disable commands-show-output -->
   ```shell
   $ python3 -m venv .venv
   $ . .venv/bin/activate
   ```
   <!-- markdownlint-enable commands-show-output -->

3. Go to the application source code and install Python requirements:

   ```shell
   $ cd app/
   $ pip install -r requirements.txt
   # ...
   ```

4. Make a contribution and [test](README.md#test) the changes.

5. If your change meets [SLOs](README.md#sla-slis-and-slos), commit and push
   the changes.

   ```shell
   $ cz commit
   # ...
   $ git push
   # ...
   ```

### Improving The Documentation

<!-- TODO -->

## Styleguides

### Commit Messages

See [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

### Python

See [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/).

### Shell

See [Shell Style Guide](https://google.github.io/styleguide/shellguide.html).

### Markdown

See [Markdown style guide](https://google.github.io/styleguide/docguide/style.html)

### Docker

See [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

### Makefile

See [Makefile Conventions (GNU Coding Standards)](https://www.gnu.org/prep/standards/html_node/Makefile-Conventions.html).

## Join The Project Team

<!-- TODO -->

## Attribution <!-- omit in toc -->

This guide is based on the **contributing-gen**. [Make your own](https://github.com/bttger/contributing-gen)!

[Maciej Strzelecki]: mailto:mstrzele@users.noreply.github.com
