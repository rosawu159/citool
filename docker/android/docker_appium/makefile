image = "icl/docker-appium:0.2"
container = "Appium_container"
path= "/home/icl/docker-storage/Appium:/data"
#path="Storage"
adbpath="5037:5037"
port="7878:7878"
appiumport="4723:4723"
#port="2020:2020"

image:
	docker build -t ${image} --network my-net .
run:
	#docker run -dt --network my-net -p ${port} --name ${container} --volumes-from ${path} ${image}
	docker run -dt --privileged -v /dev/bus/usb:/dev/bus/usb --network my-net -p ${port} -p ${adbpath} --name ${container} -v ${path} ${image}
exec:
	docker exec -it ${container} bash
clean:
	docker stop ${container}
	docker rm ${container}

cleani:
	docker rmi ${image}

