
image = "icl/docker-appium"
container = "Appium"
#path= "/home/icl/docker-storage:/daata"
path="Storage"
port="7878:7878"

image:
	docker build -t ${image} --network my-net .

run:
	docker run -dt --network my-net -p ${port} --name ${container} --volumes-from ${path} ${image}
exec:
	docker exec -it ${container} bash

clean:
	docker stop ${container}
	docker rm ${container}

cleani:
	docker rmi ${image}

