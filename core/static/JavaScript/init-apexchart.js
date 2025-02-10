document.addEventListener("DOMContentLoaded", function() {
    !function (r) {
        var e = function () {
            r(window).width();
            return {
                load: function () {
                    new ApexCharts(document.querySelector("#progressChart"), {
                        series: [82],
                        chart: {
                            type: "radialBar",
                            offsetY: -15,
                            height: "240px"
                        },
                        plotOptions: {
                            radialBar: {
                                startAngle: -135,
                                endAngle: 135,
                                hollow: {
                                    size: "80%"
                                },
                                track: {
                                    background: "var(--bs-primary-bg-subtle)",
                                    strokeWidth: "80%"
                                },
                                dataLabels: {
                                    name: {
                                        show: !1
                                    },
                                    value: {
                                        offsetY: 15,
                                        fontSize: "50px",
                                        color: "var(--bs-primary)",
                                        fontWeight: "600",
                                        fontFamily: "var(--font-family-base)"
                                    }
                                }
                            }
                        },
                        stroke: {
                            lineCap: "round"
                        },
                        colors: ["var(--bs-primary)"]
                    }).render()
                }
            }
        }();
        jQuery(window).on("load", function () {
            setTimeout(function () {
                e.load()
            }, 500)
        })
    }(jQuery);
})