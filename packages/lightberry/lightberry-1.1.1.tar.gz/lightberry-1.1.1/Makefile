.PHONY: proto clean 2to3

PROTO_DIR := protofiles
PROTO_OUT := lightberry/proto
PROTO_SRCS := $(wildcard ${PROTO_DIR}/*.proto)
PROTO_PY := $(PROTO_SRCS:${PROTO_DIR}/%.proto=${PROTO_OUT}/%.py) ${PROTO_OUT}/__init__.py

proto: ${PROTO_PY} 2to3

clean:
	rm -f ${PROTO_OUT}/*.py*

2to3:
	2to3 -wn ${PROTO_OUT}

${PROTO_OUT}/__init__.py:
	touch $@

${PROTO_OUT}/%.py: ${PROTO_DIR}/%.proto
	protoc --python_out=${PROTO_OUT} --mypy_out=${PROTO_OUT} $(INCLUDES:%=-I%) -I${PROTO_DIR} $^
	# mv $(@:%.py=%_pb2.py) $@
	# mv $(@:%.py=%_pb2.pyi) $(@:%.py=%.pyi)
