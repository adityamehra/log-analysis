This tutorial is taken from Udacity's Full Stack Web Developer Nanodegree.

# Prerequisites

- VirtualBox, see [VirtualBox](#install-virtualbox) section
- Vagrant, see [Vagrant](#install-vagrant) section
- VM configuration, see [Download the VM configuration](#download-the-vm-configuration) section

# How to run the code

- Fork and clone the repository https://github.com/adityamehra/log-analysis or download the repository.
- Install the prerequisites
- Setup the data
- Data is in newsdata.zip, see [Data](#data) section for setting up the data.
- Use the command 'python log_analysis_db.py' to get the results

# Data

After cloning/downloading this repo you will need to unzip 'newsdata.zip'. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To load the data, use the command `psql -d news -f newsdata.sql`.
Here's what this command does:

- `psql` — the PostgreSQL command line program
- `-d news` — connect to the database named news which has been set up for you
- `-f newsdata.sql` — run the SQL statements in the file newsdata.sql

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## Explore the data
Once you have the data loaded into your database, connect to your database using `psql -d news` and explore the tables using the `\dt` and `\d` table commands and select statements.

- \dt — display tables — lists the tables that are available in the database.
- \d table — (replace table with the name of a table) — shows the database schema for that particular table.

Get a sense for what sort of information is in each column of these tables.

The database includes three tables:

- The __authors__ table includes information about the authors of articles.
- The __articles__ table includes the articles themselves.
- The __log__ table includes one entry for each time a user has accessed the site.

As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.

# How to setup VirtualBox and Vagrant

## Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. [You can download it from virtualbox.org, here](https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

__Ubuntu users__: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

## Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

__Windows users__ The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

- If Vagrant is successfully installed, you will be able to run `vagrant --version` in your terminal to see the version number.
- The shell prompt in your terminal may differ. Here, the `$` sign is the shell prompt.

## Download the VM configuration

You can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm or download the repository.

You will end up with a new directory containing the VM files. Change to this directory in your terminal with `cd`. Inside, you will find another directory called __vagrant__. Change directory to the __vagrant__ directory.

## Start the virtual machine

From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
- Starting the Ubuntu Linux installation with `vagrant up`.

When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!
