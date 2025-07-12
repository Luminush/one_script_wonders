{% for frame in frames %}

struct Frame_{{frame.frame_name}} {

	uint32_t frameID = {{frame.frame_id}};
	{% for entry in entries -%}
	{% if entry.frame_id == frame.frame_id -%}
	{% if entry.stop_bit - entry.starting_bit < 8 %}uint8_t {{entry.signal_name}} : {{entry.stop_bit - entry.starting_bit}}; 
	{% elif entry.stop_bit - entry.starting_bit < 16 %}uint16_t {{entry.signal_name}} : {{entry.stop_bit - entry.starting_bit}};
       	{% elif entry.stop_bit - entry.starting_bit < 32 %}uint32_t {{entry.signal_name}} : {{entry.stop_bit - entry.starting_bit}};
	{% endif -%}
	{% endif %}
	{%- endfor %}
}
{% endfor -%}
