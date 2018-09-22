image = "icl/docker-android"
container = "Android_container"
user="android_user"
path= "${HOME}/docker-storage/Android:/home/${user}/Android"
vncPort="5901:5901"


image:
	docker build -t ${image} --network my-net .
run:
	docker run -dt --network my-net -p ${vncPort}  --name ${container} -v ${path} ${image}
exec:
	docker exec -it ${container} bash
clean:
	docker stop ${container}
	docker rm ${container}
cleani:
	docker rmi ${image}
