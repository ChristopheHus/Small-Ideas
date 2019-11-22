#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_TEXTURE_SHADER

varying vec4 vertTexCoord;
uniform sampler2D texture;
uniform int blurRad;
uniform float sigma;
uniform vec2 texOffset;
uniform vec2 blurVec;
const float PI = 3.14159265;

void main()
{  
	vec2 p = vertTexCoord.st;

	vec3 incrementalGaussian;
	incrementalGaussian.x = 1.0 / (sqrt(2.0 * PI) * sigma);
	incrementalGaussian.y = exp(-0.5 / (sigma * sigma));
	incrementalGaussian.z = incrementalGaussian.y * incrementalGaussian.y;

	vec4 avgValue = vec4(0.0, 0.0, 0.0, 0.0);
	float coefficientSum = 0.0;

	avgValue += texture2D(texture, p) * incrementalGaussian.x;
	coefficientSum += incrementalGaussian.x;
	incrementalGaussian.xy *= incrementalGaussian.yz;

	for (float i = 1.0; i <= blurRad; i++)
	{ 
		avgValue += texture2D(texture, p - i * texOffset * blurVec) * incrementalGaussian.x;         
		avgValue += texture2D(texture, p + i * texOffset * blurVec) * incrementalGaussian.x;         
		coefficientSum += 2.0 * incrementalGaussian.x;
		incrementalGaussian.xy *= incrementalGaussian.yz;
	}

	gl_FragColor = avgValue / coefficientSum;
}