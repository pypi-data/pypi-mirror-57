import os
import unittest

import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
from tecplot.plot.slice import (SliceContour, SliceGroup, SliceEffects,
                                SliceVector, SliceEdge, SliceMesh, SliceShade)

from ..sample_data import sample_data
from tecplot.tecutil import Index
from ..property_test import PropertyTest
from test import patch_tecutil, skip_on
from tecplot.plot import ContourGroup

from test import skip_on, skip_if_sdk_version_before, mocked_sdk_version


class TestSlice(PropertyTest):
    def setUp(self):
        tp.new_layout()
        self.filename, self.dataset = sample_data('2x2x3_overlap')
        frame = tp.active_frame()
        self.frame = frame

        frame.plot_type = PlotType.Cartesian3D
        self.plot = frame.plot()
        self.slice = self.plot.slice(0)  # type: SliceGroup

    def tearDown(self):
        tp.new_layout()
        os.remove(self.filename)

    @skip_if_sdk_version_before(2017, 3)
    def test_extract(self):
        nzones = self.dataset.num_zones
        new_zone = self.slice.extract()
        self.assertIsInstance(new_zone, tp.data.zone.Zone)
        self.assertEqual(self.dataset.num_zones, nzones + 1)

        nzones = self.dataset.num_zones
        new_zones = self.slice.extract(
            mode=ExtractMode.OneZonePerConnectedRegion,
            assign_strand_ids=False,
            resulting_1d_zone_type=Resulting1DZoneType.FELineSegment)
        new_zones = list(new_zones)
        self.assertGreater(len(new_zones), 0)
        self.assertIsInstance(new_zones[0], tp.data.zone.Zone)
        self.assertEqual(self.dataset.num_zones, nzones + len(new_zones))

        with patch_tecutil('ExtractSlicesX', return_value=False):
            with self.assertRaises((TecplotSystemError, TecplotLogicError)):
                self.slice.extract()

        if __debug__:
            with mocked_sdk_version(2017, 2):
                with self.assertRaises(TecplotOutOfDateEngineError):
                    self.slice.extract()

    @skip_if_sdk_version_before(2019, 1)
    def test_extract_transient(self):
        self.dataset.zone(0).strand = 1
        self.dataset.zone(0).solution_time = 1.0
        self.dataset.zone(1).strand = 1
        self.dataset.zone(1).solution_time = 2.0
        self.plot.active_fieldmap_indices = [0, 1]
        self.plot.solution_time = 1.0

        z = self.slice.extract(
            transient_mode=TransientOperationMode.AllSolutionTimes)
        z = list(z)
        self.assertGreater(len(z), 1)

        self.assertTrue(tp.tecutil._tecutil.DataSetJournalIsValid())

    def test_set_arbitrary(self):
        p1 = (1, 2, 3)
        p2 = (4, 5, 6)
        p3 = (.7, .8, .9)

        self.plot.show_slices = True
        self.slice.orientation = SliceSurface.Arbitrary
        self.slice.set_arbitrary_from_points(p1, p2, p3)

        self.assertAlmostEqual(self.slice.arbitrary_normal[0], -2.7)
        self.assertAlmostEqual(self.slice.arbitrary_normal[1], 5.4)
        self.assertAlmostEqual(self.slice.arbitrary_normal[2], -2.7)
        self.assertEqual(self.slice.origin, (.7, .8, .9))

    def test_set_arbitrary_failure(self):
        with patch_tecutil('SliceSetArbitraryUsingThreePoints') as set_arb:
            set_arb.return_value = False
            with self.assertRaises(TecplotSystemError):
                p1 = (1, 2, 3)
                p2 = (4, 5, 6)
                p3 = (.7, .8, .9)
                self.slice.set_arbitrary_from_points(p1, p2, p3)

    def test_contour(self):
        self.assertIsInstance(self.slice.contour, SliceContour)
        with self.assertRaises(AttributeError):
            self.slice.contour = None

    def test_mesh(self):
        self.assertIsInstance(self.slice.mesh, SliceMesh)
        with self.assertRaises(AttributeError):
            self.slice.mesh = None

    def test_effects(self):
        self.assertIsInstance(self.slice.effects, SliceEffects)
        with self.assertRaises(AttributeError):
            self.slice.effects = None

    def test_edge(self):
        self.assertIsInstance(self.slice.edge, SliceEdge)
        with self.assertRaises(AttributeError):
            self.slice.edge = None

    def test_shade(self):
        self.assertIsInstance(self.slice.shade, SliceShade)
        with self.assertRaises(AttributeError):
            self.slice.shade = None

    def test_vector(self):
        self.assertIsInstance(self.slice.vector, SliceVector)
        with self.assertRaises(AttributeError):
            self.slice.vector = None

    def test_eq(self):
        slice_0 = self.plot.slice(0)
        self.assertTrue(slice_0 == self.plot.slice(0))
        self.assertTrue(slice_0 != self.plot.slice(1))
        self.assertFalse(slice_0 == self.plot.slice(1))
        self.assertFalse(slice_0 != self.plot.slice(0))

    def test_slice_group_round_trip(self):
        for api, value in (
                ('show', bool),
                ('arbitrary_normal', (1.0, 2.0, 3.0)),
                ('show_primary_slice', bool),
                ('slice_source', SliceSource),
                ('show_start_and_end_slices', bool),
                ('obey_source_zone_blanking', bool),
                ('show_intermediate_slices', bool),
                ('num_intermediate_slices', 1)):
            self.internal_test_property_round_trip(
                api, value, SliceGroup, self.slice)

    def test_start_position(self):
        self.slice.orientation = SliceSurface.IPlanes
        self.slice.start_position = (0, 1, 2)
        self.assertAllClose(self.slice.start_position, (0, 1, 2))

        self.slice.start_position = (3, 5, 7)
        self.assertAllClose(self.slice.start_position, (3, 5, 7))

        self.slice.start_position.i = 2
        self.slice.start_position.j = 3
        self.slice.start_position.k = 4
        self.assertEqual(self.slice.start_position.i, 2)
        self.assertEqual(self.slice.start_position.j, 3)
        self.assertEqual(self.slice.start_position.k, 4)

        self.slice.orientation = SliceSurface.Arbitrary
        self.slice.start_position = (0, 1, 2)
        self.assertAllClose(self.slice.start_position, (0, 1, 2))

        self.slice.start_position = (3, 5, 7)
        self.assertAllClose(self.slice.start_position, (3, 5, 7))

        self.slice.start_position.x = 2
        self.slice.start_position.y = 3
        self.slice.start_position.z = 4
        self.assertAlmostEqual(self.slice.start_position.x, 2)
        self.assertAlmostEqual(self.slice.start_position.y, 3)
        self.assertAlmostEqual(self.slice.start_position.z, 4)

    def test_end_position(self):
        self.slice.orientation = SliceSurface.IPlanes
        self.slice.end_position = (0, 1, 2)
        self.assertAllClose(self.slice.end_position, (0, 1, 2))

        self.slice.end_position = (3, 5, 7)
        self.assertAllClose(self.slice.end_position, (3, 5, 7))

        self.slice.end_position.i = 2
        self.slice.end_position.j = 3
        self.slice.end_position.k = 4
        self.assertEqual(self.slice.end_position.i, 2)
        self.assertEqual(self.slice.end_position.j, 3)
        self.assertEqual(self.slice.end_position.k, 4)

        self.slice.orientation = SliceSurface.Arbitrary
        self.slice.end_position = (0, 1, 2)
        self.assertAllClose(self.slice.end_position, (0, 1, 2))

        self.slice.end_position = (3, 5, 7)
        self.assertAllClose(self.slice.end_position, (3, 5, 7))

        self.slice.end_position.x = 2
        self.slice.end_position.y = 3
        self.slice.end_position.z = 4
        self.assertAlmostEqual(self.slice.end_position.x, 2)
        self.assertAlmostEqual(self.slice.end_position.y, 3)
        self.assertAlmostEqual(self.slice.end_position.z, 4)

    @skip_if_sdk_version_before(2017, 2)
    @skip_on(TecplotOutOfDateEngineError)
    def test_surface_generation_method(self):
        if __debug__:
            with mocked_sdk_version(2017, 2):
                with self.assertRaises(TecplotOutOfDateEngineError):
                    self.slice.surface_generation_method = \
                        SurfaceGenerationMethod.AllPolygons

                for val in [SurfaceGenerationMethod.AllowQuads,
                            SurfaceGenerationMethod.AllTriangles]:
                    self.slice.surface_generation_method = val
                    self.assertEqual(self.slice.surface_generation_method, val)
        elif tp.sdk_version_info < (2018, 1):
            raise unittest.SkipTest('Changed in SDK in 2018.1')

        for val in SurfaceGenerationMethod:
            self.slice.surface_generation_method = val
            self.assertEqual(self.slice.surface_generation_method, val)

    def test_slice_ijk_position(self):
        # Use origin as representative ijk
        for slice_surface in (SliceSurface.IPlanes,
                              SliceSurface.JPlanes,
                              SliceSurface.KPlanes):

            self.slice.orientation = slice_surface
            self.slice.origin = (1, 2, 3)
            self.assertEqual(self.slice.origin.i, 1)
            self.assertEqual(self.slice.origin.j, 2)
            self.assertEqual(self.slice.origin.k, 3)

            if __debug__:
                for bad_attribute in ('x', 'y', 'z'):
                    with self.assertRaises(AttributeError):
                        getattr(self.slice.origin, bad_attribute)

            self.slice.origin += (1, 1, 1)
            self.assertEqual(self.slice.origin, (2, 3, 4))

            self.slice.origin -= (1, 1, 1)
            self.assertEqual(self.slice.origin, (1, 2, 3))

            with self.assertRaises(TecplotSystemError):
                self.slice.origin = -self.slice.origin

            slice_1 = self.plot.slice(1)  # type: SliceGroup
            slice_1.orientation = slice_surface
            slice_1.origin = (1, 2, 3)
            self.slice.origin = slice_1.origin
            self.assertEqual(self.slice.origin.i, 1)
            self.assertEqual(self.slice.origin.j, 2)
            self.assertEqual(self.slice.origin.k, 3)

            self.slice.origin += slice_1.origin
            self.assertEqual(self.slice.origin, (2, 4, 6))

            self.slice.origin -= slice_1.origin
            self.assertEqual(self.slice.origin, (1, 2, 3))

            self.slice.origin[0] = 1
            self.assertEqual(self.slice.origin.i, 1)

            with self.assertRaises(IndexError):
                self.slice.origin[4]

            self.slice.origin = (0, 1, 2)
            self.assertEqual('(0, 1, 2)', str(self.slice.origin))

            with self.assertRaises(TypeError):
                self.slice.origin = 1

            with self.assertRaises(TypeError):
                self.slice.origin += 2

    def test_slice_xyz_position(self):
        # Use origin as the representative xyz
        for slice_surface in (SliceSurface.XPlanes,
                              SliceSurface.YPlanes,
                              SliceSurface.ZPlanes):

            self.slice.orientation = slice_surface
            self.slice.origin = (1.1, 2, 3)
            self.assertEqual(self.slice.origin.x, 1.1)
            self.assertEqual(self.slice.origin.y, 2.0)
            self.assertEqual(self.slice.origin.z, 3.0)

            if __debug__:
                for bad_attribute in ('i', 'j', 'k'):
                    with self.assertRaises(AttributeError):
                        getattr(self.slice.origin, bad_attribute)

            self.slice.origin += (1, 2, 3)
            self.assertEqual(self.slice.origin, (2.1, 4.0, 6.0))

            self.slice.origin -= (1, 2, 3)
            self.assertEqual(self.slice.origin, (1.1, 2.0, 3.0))

            self.slice.origin = -self.slice.origin
            self.assertEqual(self.slice.origin, (-1.1, -2.0, -3.0))

            slice_1 = self.plot.slice(1)  # type: SliceGroup
            slice_1.orientation = slice_surface
            slice_1.origin = (1.1, 2, 3)
            self.slice.origin = slice_1.origin
            self.assertEqual(self.slice.origin.x, 1.1)
            self.assertEqual(self.slice.origin.y, 2.0)
            self.assertEqual(self.slice.origin.z, 3.0)

            self.slice.origin += slice_1.origin
            self.assertEqual(self.slice.origin, (2.2, 4, 6))

            self.slice.origin -= slice_1.origin
            self.assertEqual(self.slice.origin, (1.1, 2.0, 3.0))

            self.slice.origin = -self.slice.origin
            self.assertEqual(self.slice.origin, (-1.1, -2.0, -3.0))

            with self.assertRaises(TypeError):
                self.slice.origin = 1

            with self.assertRaises(TypeError):
                self.slice.origin += 2

    def test_slice_contour_round_trip(self):
        for api, value in (
                ('show', bool),
                ('line_color', Color),
                ('line_thickness', 0.5),
                ('contour_type', ContourType),
                ('flood_contour_group_index', 1),
                ('flood_contour_group', ContourGroup(1, self.plot)),
                ('use_lighting_effect', bool),
                ('line_contour_group_index', Index),
                ('line_contour_group', ContourGroup(1, self.plot))
                 ):
            self.internal_test_property_round_trip(
                api, value, SliceContour, self.slice.contour)

    def test_slice_effects_round_trip(self):
        for api, value in (
                ('lighting_effect', LightingEffect),
                ('surface_translucency', 1),
                ('use_translucency', bool)
                 ):
            self.internal_test_property_round_trip(
                api, value, SliceEffects, self.slice.effects)

    def test_slice_mesh_round_trip(self):
        for api, value in (
                ('line_thickness', 1.0),
                ('show', bool),
                ('color', Color),
                 ):
            self.internal_test_property_round_trip(
                api, value, SliceMesh, self.slice.mesh)

    def test_slice_shade_round_trip(self):
        for api, value in (
                ('use_lighting_effect', bool),
                ('show', bool),
                ('color', Color),
        ):
            self.internal_test_property_round_trip(
                api, value, SliceShade, self.slice.shade)

    def test_slice_edge_round_trip(self):
        for api, value in (
                ('show', bool),
                ('color', Color),
                ('line_thickness', .01),
                ('edge_type', EdgeType)
                 ):
            self.internal_test_property_round_trip(
                api, value, SliceEdge, self.slice.edge)


class TestSliceVector(unittest.TestCase):
    def setUp(self):
        tp.new_layout()
        self.filename, self.dataset = sample_data('3x3x3_p')
        frame = tp.active_frame()
        frame.plot_type = PlotType.Cartesian3D
        plot = frame.plot(PlotType.Cartesian3D)
        plot.vector.u_variable = self.dataset.variable(0)
        plot.vector.v_variable = self.dataset.variable(1)
        plot.vector.w_variable = self.dataset.variable(2)
        self.vec = frame.plot().slice(0).vector

    def tearDown(self):
        tp.new_layout()
        os.remove(self.filename)

    def test_show(self):
        for val in [True, False, True]:
            self.vec.show = val
            self.assertEqual(self.vec.show, val)

    def test_is_tangent(self):
        for val in [True, False, True]:
            self.vec.is_tangent = val
            self.assertEqual(self.vec.is_tangent, val)

    def test_color(self):
        for val in [Color.Black, Color.Red, Color.Blue]:
            self.vec.color = val
            self.assertEqual(self.vec.color, val)
        with self.assertRaises(ValueError):
            self.vec.color = 0.5

    def test_line_thickness(self):
        for val in [0.5, 1, 2, 100]:
            self.vec.line_thickness = val
            self.assertAlmostEqual(self.vec.line_thickness, val)
        with self.assertRaises(ValueError):
            self.vec.line_thickness = 'badtype'
        with self.assertRaises(TecplotSystemError):
            self.vec.line_thickness = -1
        with self.assertRaises(TecplotSystemError):
            self.vec.line_thickness = 0
        with self.assertRaises(TecplotSystemError):
            self.vec.line_thickness = 101

    def test_vector_type(self):
        for val in [VectorType.TailAtPoint, VectorType.HeadAtPoint,
                    VectorType.MidAtPoint]:
            self.vec.vector_type = val
            self.assertEqual(self.vec.vector_type, val)
        with self.assertRaises(ValueError):
            self.vec.vector_type = 0.5

    def test_arrowhead_style(self):
        for val in [ArrowheadStyle.Plain, ArrowheadStyle.Filled,
                    ArrowheadStyle.Hollow]:
            self.vec.arrowhead_style = val
            self.assertEqual(self.vec.arrowhead_style, val)
        with self.assertRaises(ValueError):
            self.vec.arrowhead_style = 0.5


if __name__ == '__main__':
    from .. import main
    main()
