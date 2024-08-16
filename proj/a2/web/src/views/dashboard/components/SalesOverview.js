import React, {useEffect, useState} from 'react';
import { Select, MenuItem } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import DashboardCard from '../../../components/shared/DashboardCard';
import Chart from 'react-apexcharts';
import {dtsTable} from "../../../api/utils";


const SalesOverview = () => {
    const [tableData, setTableData] = useState([]);

    useEffect(() => {
        const fetchTableData = async () => await dtsTable("operating_cash_balance").catch((err) => {
            console.log(err);
        });
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
            height: 350,
            type: 'line',
            dropShadow: {
                enabled: true,
                color: '#000',
                top: 18,
                left: 7,
                blur: 10,
                opacity: 0.2
            },
            zoom: {
                enabled: false
            },
            toolbar: {
                show: false
            }
        },
        colors: ['#77B6EA', '#545454'],
        dataLabels: {
            enabled: true,
        },
        stroke: {
            curve: 'smooth'
        },
        // title: {
        //     text: 'Average High & Low Temperature',
        //     align: 'left'
        // },
        grid: {
            borderColor: '#e7e7e7',
            row: {
                colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                opacity: 0.5
            },
        },
        markers: {
            size: 1
        },
        xaxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
            title: {
                text: 'Day'
            }
        },
        yaxis: {
            title: {
                text: 'Net change'
            },
            min: 5,
            max: 40
        },
        legend: {
            position: 'top',
            horizontalAlign: 'right',
            floating: true,
            offsetY: -25,
            offsetX: -5
        }
    }

    const seriescolumnchart = [
        {
            name: "High - 2013",
            data: [28, 29, 33, 36, 32, 32, 33]
        },
        // {
        //     name: "Low - 2013",
        //     data: [12, 11, 14, 18, 17, 13, 13]
        // }
        // {
        //     name: 'Eanings this month',
        //     data: [{ x: '05/06/2014', y: 54 }, { x: '05/08/2014', y: 17 }, { x: '05/28/2014', y: 26 }],
        // },
        // {
        //     name: 'Expense this month',
        //     data: [{ x: '05/06/2014', y: 4 }, { x: '05/08/2014', y: 55 }, { x: '05/28/2014', y: 236 }],
        // },
        // {
        //     name: 'Expense this month 1',
        //     data: [{ x: '05/06/2014', y: 541 }, { x: '05/08/2014', y: 417 }, { x: '05/28/2014', y: 226 }],
        // },
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
                type="line"
                height="370px"
            />
        </DashboardCard>
    );
};

export default SalesOverview;
