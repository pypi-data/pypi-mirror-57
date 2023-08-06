"""A distortion of the scene inwards/outwards."""
from dataclasses import dataclass

import moderngl

from ..shaders import bind_framebuffer
from .base import PostprocessPass


DISTORT_PROG = """ \
#version 330 core

in vec2 uv;
out vec4 f_color;

uniform sampler2D fb;

uniform float factor;

const vec2 center = vec2(0.5, 0.5);

void main()
{
    vec2 off = uv - center;

    float dist = pow(length(off) * 2, factor) / 2;

    off = dist * normalize(off);

    f_color = texture(fb, center + off);
}

"""


@dataclass
class Punch:
    """A distortion of the scene inwards/outwards."""
    ctx: moderngl.Context
    factor: float = 0.9

    camera: 'wasabi2d.scene.Camera' = None
    _pass: PostprocessPass = None
    _fb: moderngl.Framebuffer = None

    def _set_camera(self, camera: 'wasabi2d.scene.Camera'):
        """Resize the effect for this viewport."""
        self.camera = camera
        self._pass = PostprocessPass(
            self.ctx,
            DISTORT_PROG,
        )

    def draw(self, draw_layer):
        with self.camera.temporary_fbs(1, 'f2') as (fb,):
            with bind_framebuffer(self.ctx, fb, clear=True):
                draw_layer()

            self._pass.render(
                fb=fb,
                factor=self.factor,
            )
