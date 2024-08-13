import React, {useEffect, useState} from 'react';
import { Select, MenuItem } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import DashboardCard from '../../../components/shared/DashboardCard';
import Chart from 'react-apexcharts';
import {dtsTable} from "../../../api/utils";


const SalesOverview = () => {
    const [tableData, setTableData] = useState([]);

    useEffect(async () => {
        const fetchTableData = async () => await dtsTable("operating_cash_balance");
        fetchTableData().then((tableData) => {
            setTableData(tableData);
        })
    }, []);

    // select
    const [month, setMonth] = useState('1');

    const handleChange = (event) => {
        setMonth(event.target.value);
    };

    // chart color
    const theme = useTheme();
    const primary = theme.palette.primary.main;
    const secondary = theme.palette.secondary.main;

    // chart
    const optionscolumnchart = {
        chart: {
            type: 'area',
            stacked: false,
            height: 350,
            zoom: {
                type: 'x',
                enabled: true,
                autoScaleYaxis: true
            },
            toolbar: {
                autoSelected: 'zoom'
            }
        },
        dataLabels: {
            enabled: false
        },
        markers: {
            size: 0,
        },
        // title: {
        //     text: 'Stock Price Movement',
        //     align: 'left'
        // },
        fill: {
            type: 'gradient',
            gradient: {
                shadeIntensity: 1,
                inverseColors: false,
                opacityFrom: 0.5,
                opacityTo: 0,
                stops: [0, 90, 100]
            },
        },
        yaxis: {
            labels: {
                formatter: function (val) {
                    return (val / 1000000).toFixed(0);
                },
            },
            title: {
                text: 'Price'
            },
        },
        xaxis: {
            type: 'datetime',
        },
        tooltip: {
            shared: false,
            y: {
                formatter: function (val) {
                    return (val / 1000000).toFixed(0)
                }
            }
        }
    };
    const seriescolumnchart = [
        {
            name: 'Eanings this month',
            data: [{ x: '05/06/2014', y: 54 }, { x: '05/08/2014', y: 17 }, { x: '05/28/2014', y: 26 }],
        },
        {
            name: 'Expense this month',
            data: [{ x: '05/06/2014', y: 4 }, { x: '05/08/2014', y: 55 }, { x: '05/28/2014', y: 236 }],
        },
        {
            name: 'Expense this month 1',
            data: [{ x: '05/06/2014', y: 541 }, { x: '05/08/2014', y: 417 }, { x: '05/28/2014', y: 226 }],
        },
    ];

    return (

        <DashboardCard title="Operating Cash Balance" action={
            <Select
                labelId="month-dd"
                id="month-dd"
                value={month}
                size="small"
                onChange={handleChange}
            >
                <MenuItem value={1}>March 2023</MenuItem>
                <MenuItem value={2}>April 2023</MenuItem>
                <MenuItem value={3}>May 2023</MenuItem>
            </Select>
        }>
            <Chart
                options={optionscolumnchart}
                series={seriescolumnchart}
                type="area"
                height="370px"
            />
        </DashboardCard>
    );
};

export default SalesOverview;
