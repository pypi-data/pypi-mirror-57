# -*- coding: utf-8 -*-
# surf.py
"""
sfftk.formats.stl
==================
User-facing reader classes for Stereolithography files
"""
from __future__ import division, print_function

import inspect
import os.path

from .base import Segmentation, Header, Segment, Annotation, Mesh
from .. import schema
from ..core import _xrange, _dict_iter_values, _dict_iter_items
from ..core.print_tools import print_date
from ..readers import stlreader

__author__ = "Paul K. Korir, PhD"
__email__ = "pkorir@ebi.ac.uk, paul.korir@gmail.com"
__date__ = "2016-11-11"


class STLMesh(Mesh):
    """Mesh class"""

    def __init__(self, vertices, polygons):
        self._vertices = vertices
        self._polygons = polygons

    @property
    def vertices(self):
        """Vertices in this mesh"""
        return self._vertices

    @property
    def polygons(self):
        """Polygons in this mesh"""
        return self._polygons

    def convert(self):
        """Convert to a :py:class:`sfftk.schema.SFFMesh` object"""
        schema.SFFMesh.reset_id()
        mesh = schema.SFFMesh()
        # polygon
        polygons = schema.SFFPolygonList()
        schema.SFFPolygon.reset_id()
        for P in _dict_iter_values(self.polygons):
            polygon = schema.SFFPolygon()

            v1, v2, v3 = P
            polygon.add_vertex(v1)
            polygon.add_vertex(v2)
            polygon.add_vertex(v3)

            polygons.add_polygon(polygon)
        # vertices
        vertices = schema.SFFVertexList()
        for vertex_id, v in _dict_iter_items(self.vertices):
            x, y, z = v
            vertex = schema.SFFVertex(vID=vertex_id, x=x, y=y, z=z)
            vertices.add_vertex(vertex)
        # final tying
        mesh.vertices = vertices
        mesh.polygons = polygons
        return mesh


class STLAnnotation(Annotation):
    """Annotation class"""

    def __init__(self, name):
        self.name = name
        import random
        self.colour = tuple([random.random() for _ in _xrange(3)])

    def convert(self):
        """Convert to a :py:class:`sfftk.schema.SFFBiologicalAnnotation` object"""
        annotation = schema.SFFBiologicalAnnotation()
        annotation.name = self.name
        annotation.description = None
        annotation.numberOfInstances = 1
        red, green, blue = self.colour
        colour = schema.SFFRGBA(
            red=red,
            green=green,
            blue=blue,
        )
        return annotation, colour


class STLSegment(Segment):
    """Segment class"""

    def __init__(self, name, vertices, polygons):
        self._name = name
        self._vertices = vertices
        self._polygons = polygons

    @property
    def name(self):
        """Segment name"""
        return self._name

    @property
    def annotation(self):
        """Segmentation annotation"""
        return STLAnnotation(self.name)

    @property
    def meshes(self):
        """Segment meshes"""
        return [STLMesh(self._vertices, self._polygons)]

    def convert(self):
        """Convert to a :py:class:`sfftk.schema.SFFSegment` object"""
        segment = schema.SFFSegment()
        segment.biologicalAnnotation, segment.colour = self.annotation.convert()
        meshes = schema.SFFMeshList()
        for mesh in self.meshes:
            meshes.add_mesh(mesh.convert())
        segment.meshes = meshes
        return segment


class STLHeader(Header):
    """Class definition for header in an STL segmentation file"""

    def __init__(self, segmentation):
        """Initialise an STLHeader object

        :param segmentation: raw segmentation obtained from :py:func:`sfftk.readers.stlreader.get_data` function
        """
        self._segmentation = segmentation

        for attr in dir(self._segmentation):
            if attr[:1] == "_":
                continue
            elif inspect.ismethod(getattr(self._segmentation, attr)):
                continue
            else:
                setattr(self, attr, getattr(self._segmentation, attr))

    def convert(self):
        """Convert to an EMDB-SFF segmentation header

        Currently not implemented"""
        pass


class STLSegmentation(Segmentation):
    """Class representing an STL segmentation
    
    .. code:: python
    
        from sfftk.formats.stl import STLSegmentation
        stl_seg = STLSegmentation('file.stl')
        
    """

    def __init__(self, fns, *args, **kwargs):
        self._fns = fns
        self._segments = list()
        for fn in self._fns:
            print_date("{}: Stereolithography mesh".format(os.path.basename(fn)))
            segment = stlreader.get_data(fn, *args, **kwargs)
            for name, vertices, polygons in segment:
                self._segments.append(STLSegment(name, vertices, polygons))

    @property
    def header(self):
        """The header in the segmentation"""
        return STLHeader(self._segments[0])

    @property
    def segments(self):
        """The segments in the segmentation"""
        return self._segments

    def convert(self, args, *_args, **_kwargs):
        """Convert to a :py:class:`sfftk.schema.SFFSegmentation` object"""
        segmentation = schema.SFFSegmentation()

        segmentation.name = "STL Segmentation"
        segmentation.software = schema.SFFSoftware(
            name="Unknown",
            version="Unknown",
        )
        segmentation.transforms = schema.SFFTransformList()
        segmentation.transforms.add_transform(
            schema.SFFTransformationMatrix(
                rows=3,
                cols=4,
                data='1.0 0.0 0.0 1.0 0.0 1.0 0.0 1.0 0.0 0.0 1.0 1.0'
            )
        )
        segmentation.primaryDescriptor = "meshList"

        segments = schema.SFFSegmentList()
        for s in self.segments:
            segments.add_segment(s.convert())

        segmentation.segments = segments
        # details
        if args.details is not None:
            segmentation.details = args.details
        elif 'details' in _kwargs:
            segmentation.details = _kwargs['details']
        return segmentation
