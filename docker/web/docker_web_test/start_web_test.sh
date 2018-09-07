#! /bin/bash
folder="/data/test"
testfolder="$folder/VMI_AutomaticTesting/management-portal/outsourcing/test/"
timestamp="$(date +'%Y%m%d%H%M')"
logPath="$folder/Log"


#mkdir -p $folder/Log && cd $folder && git clone https://yun0615:yunchentsai615@github.com/ItriHypervisor/VMI_AutomaticTesting.git
#cp $HOME/package.json $testfolder
#cd $testfolder && npm install
#mocha clientApiDemo.spec.js >> $logPath/$timestamp

case $1 in

	"start")
		mkdir -p $folder/Log && cd $folder && git clone https://yun0615:yunchentsai615@github.com/ItriHypervisor/VMI_AutomaticTesting.git
		cp $HOME/package.json $testfolder
		cd $testfolder && npm install
		mocha clientApiDemo.spec.js >> $logPath/$timestamp	
        ;;
        "init")
		rm -rf $folder
        ;;
        *)
		echo "e.g. ./start.sh ( start || init) "
        ;;
esac
		




